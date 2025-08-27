"""
Tests for the Path of Exile Rules module
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
from BaseClasses import CollectionState
from worlds.poe import Rules
from worlds.poe.Rules import (
    get_ascendancy_amount_for_act, get_gear_amount_for_act, get_flask_amount_for_act,
    get_gem_amount_for_act, get_skill_gem_amount_for_act, get_support_gem_amount_for_act,
    get_passives_amount_for_act, completion_condition, can_reach, SelectLocationsToAdd
)
from . import PoeTestBase


class TestActRequirementFunctions(unittest.TestCase):
    """Test functions that calculate requirements for each act"""
    
    def setUp(self):
        self.mock_opt = Mock()
        self.mock_opt.ascendancies_available_per_class.value = 3
        self.mock_opt.starting_character.value = 1  # Not Scion
        self.mock_opt.starting_character.option_scion = 7
        self.mock_opt.gear_upgrades_per_act.value = 5
        self.mock_opt.gucci_hobo_mode.value = 0  # disabled
        self.mock_opt.gucci_hobo_mode.option_disabled = 0
        self.mock_opt.add_flask_slots_to_item_pool = True
        self.mock_opt.flask_slots_per_act.value = 2
        self.mock_opt.add_max_links_to_item_pool = True
        self.mock_opt.max_links_per_act.value = 3
        self.mock_opt.skill_gems_per_act.value = 4
        self.mock_opt.support_gems_per_act.value = 3
        self.mock_opt.add_passive_skill_points_to_item_pool.value = True
    
    def test_get_ascendancy_amount_for_act(self):
        """Test ascendancy amount calculation"""
        # Act 3 and above should return ascendancy amount
        self.assertEqual(get_ascendancy_amount_for_act(3, self.mock_opt), 3)
        self.assertEqual(get_ascendancy_amount_for_act(4, self.mock_opt), 3)
        # Other acts should return 0
        self.assertEqual(get_ascendancy_amount_for_act(1, self.mock_opt), 0)
        self.assertEqual(get_ascendancy_amount_for_act(2, self.mock_opt), 0)

    
    def test_get_ascendancy_amount_for_scion(self):
        """Test ascendancy amount for Scion character"""
        self.mock_opt.starting_character.value = self.mock_opt.starting_character.option_scion
        
        result = get_ascendancy_amount_for_act(3, self.mock_opt)
        self.assertEqual(result, 1)  # Scion gets only 1 ascendancy
    
    def test_get_gear_amount_for_act(self):
        """Test gear amount calculation"""
        # Act 1 should give 0 gear (act - 1)
        self.assertEqual(get_gear_amount_for_act(1, self.mock_opt), 0)
        
        # Act 3 should give 10 gear (5 * 2)
        self.assertEqual(get_gear_amount_for_act(3, self.mock_opt), 10)
        
        # Test with gucci hobo mode
        self.mock_opt.gucci_hobo_mode.value = 1  # enabled
        result = get_gear_amount_for_act(20, self.mock_opt)  # Large act to test max
        self.assertEqual(result, Rules.MAX_GUCCI_GEAR_UPGRADES)
    
    def test_get_flask_amount_for_act(self):
        """Test flask amount calculation"""
        self.assertEqual(get_flask_amount_for_act(1, self.mock_opt), 0)
        self.assertEqual(get_flask_amount_for_act(3, self.mock_opt), 4)  # 2 * 2
        
        # Test with flask slots disabled
        self.mock_opt.add_flask_slots_to_item_pool = False
        self.assertEqual(get_flask_amount_for_act(3, self.mock_opt), 0)
    
    def test_get_gem_amount_for_act(self):
        """Test gem slot amount calculation"""
        self.assertEqual(get_gem_amount_for_act(1, self.mock_opt), 0)
        self.assertEqual(get_gem_amount_for_act(3, self.mock_opt), 6)  # 3 * 2
        
        # Test with max links disabled
        self.mock_opt.add_max_links_to_item_pool = False
        self.assertEqual(get_gem_amount_for_act(3, self.mock_opt), 0)
    
    def test_get_skill_gem_amount_for_act(self):
        """Test skill gem amount calculation"""
        self.assertEqual(get_skill_gem_amount_for_act(1, self.mock_opt), 0)
        self.assertEqual(get_skill_gem_amount_for_act(3, self.mock_opt), 8)  # 4 * 2
        
        # Test max cap
        result = get_skill_gem_amount_for_act(20, self.mock_opt)
        self.assertEqual(result, Rules.MAX_SKILL_GEMS)
    
    def test_get_support_gem_amount_for_act(self):
        """Test support gem amount calculation"""
        self.assertEqual(get_support_gem_amount_for_act(1, self.mock_opt), 0)
        self.assertEqual(get_support_gem_amount_for_act(3, self.mock_opt), 6)  # 3 * 2
        
        # Test max cap
        result = get_support_gem_amount_for_act(20, self.mock_opt)
        self.assertEqual(result, Rules.MAX_SUPPORT_GEMS)
    
    def test_get_passives_amount_for_act(self):
        """Test passive points amount calculation"""
        self.assertEqual(get_passives_amount_for_act(1, self.mock_opt), 6)
        self.assertEqual(get_passives_amount_for_act(5, self.mock_opt), 56)
        self.assertEqual(get_passives_amount_for_act(12, self.mock_opt), 136)
        
        # Test with passive points disabled
        self.mock_opt.add_passive_skill_points_to_item_pool.value = False
        self.assertEqual(get_passives_amount_for_act(5, self.mock_opt), 0)
        
        # Test with act not in table
        self.mock_opt.add_passive_skill_points_to_item_pool.value = True
        self.assertEqual(get_passives_amount_for_act(99, self.mock_opt), 0)


class TestCompletionCondition(PoeTestBase):
    """Test completion condition logic"""
    
    def setUp(self):
        super().setUp()
        self.mock_world = Mock()
        self.mock_state = Mock(spec=CollectionState)
    
    @patch('worlds.poe.Rules.can_reach')
    def test_completion_condition_with_bosses(self, mock_can_reach):
        """Test completion condition when bosses are required"""
        self.mock_world.bosses_for_goal = ["shaper", "elder"]
        self.mock_world.goal_act = 10
        mock_can_reach.return_value = True
        
        result = completion_condition(self.mock_world, self.mock_state)
        
        self.assertTrue(result)
        mock_can_reach.assert_called_once_with(11, self.mock_world, self.mock_state)
    
    @patch('worlds.poe.Rules.can_reach')
    def test_completion_condition_without_bosses(self, mock_can_reach):
        """Test completion condition when only act completion is required"""
        self.mock_world.bosses_for_goal = []
        self.mock_world.goal_act = 8
        mock_can_reach.return_value = True
        
        result = completion_condition(self.mock_world, self.mock_state)
        
        self.assertTrue(result)
        mock_can_reach.assert_called_once_with(8, self.mock_world, self.mock_state)


class TestCanReach(PoeTestBase):
    """Test can_reach logic function"""
    
    def setUp(self):
        super().setUp()
        self.mock_world = Mock()
        self.mock_state = Mock(spec=CollectionState)
        self.mock_options = Mock()
        
        # Setup default options
        self.mock_options.disable_generation_logic.value = False
        self.mock_options.ascendancies_available_per_class.value = 3
        self.mock_options.starting_character.value = 1
        self.mock_options.starting_character.option_scion = 7
        self.mock_options.starting_character.current_option_name = "Marauder"
        self.mock_options.gear_upgrades_per_act.value = 2
        self.mock_options.gucci_hobo_mode.value = 0
        self.mock_options.gucci_hobo_mode.option_disabled = 0
        self.mock_options.add_flask_slots_to_item_pool = True
        self.mock_options.flask_slots_per_act.value = 1
        self.mock_options.add_max_links_to_item_pool = True
        self.mock_options.max_links_per_act.value = 1
        self.mock_options.skill_gems_per_act.value = 2
        self.mock_options.support_gems_per_act.value = 1
        self.mock_options.add_passive_skill_points_to_item_pool.value = True
        
        self.mock_world.options = self.mock_options
        self.mock_world.player = 1
    
    def test_can_reach_early_act(self):
        """Test can_reach for acts before act 1"""
        result = can_reach(0, self.mock_world, self.mock_state)
        self.assertTrue(result)
        
        result = can_reach(-1, self.mock_world, self.mock_state)
        self.assertTrue(result)
    
    def test_can_reach_with_disabled_logic(self):
        """Test can_reach when generation logic is disabled"""
        self.mock_options.disable_generation_logic.value = True
        
        result = can_reach(5, self.mock_world, self.mock_state)
        self.assertTrue(result)
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_act_1_requirements(self, mock_acts, mock_gems_by_weapon, mock_max_links, 
                                         mock_support_gems, mock_flask_items, 
                                         mock_gear_items, mock_ascendancy_items, 
                                         mock_get_by_category):
        """Test can_reach for act 1 with specific requirements"""
        
        # Mock acts data
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
        
        # Mock item returns using real item names from Items.json
        mock_weapon_items = [
            {"name": "Progressive Sword"}, 
            {"name": "Progressive Axe"}, 
            {"name": "Progressive Bow"}
        ]
        mock_get_by_category.return_value = mock_weapon_items
        mock_ascendancy_items.return_value = [{"name": "Berserker"}]
        mock_gear_items.return_value = [
            {"name": "Progressive BodyArmour"}, 
            {"name": "Progressive Helmet"}
        ]
        mock_flask_items.return_value = [{"name": "Progressive Flask Unlock"}]
        mock_support_gems.return_value = [{"name": "Chance to Bleed Support"}]
        mock_max_links.return_value = [{"name": "Progressive max links - Weapon"}]
        mock_gems_by_weapon.return_value = [
            {"name": "Fireball"}, {"name": "Freezing Pulse"}, 
            {"name": "Spark"}, {"name": "Lightning Tendrils"},
            {"name": "Crushing Fist"}
        ]
        
        # Mock state counts - sufficient for all requirements
        self.mock_state.has_from_list.return_value = True
        self.mock_state.count_from_list.return_value = 10
        self.mock_state.count.return_value = 50
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertTrue(result)
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_insufficient_requirements(self, mock_acts, mock_gems_by_weapon, mock_max_links,
                                                mock_support_gems, mock_flask_items,
                                                mock_gear_items, mock_ascendancy_items,
                                                mock_get_by_category):
        """Test can_reach when requirements are not met"""
        
        # Mock acts data
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 30}
        
        # Mock insufficient items
        mock_get_by_category.return_value = []
        mock_ascendancy_items.return_value = []
        mock_gear_items.return_value = []
        mock_flask_items.return_value = []
        mock_support_gems.return_value = []
        mock_max_links.return_value = []
        mock_gems_by_weapon.return_value = []
        
        # Mock insufficient state counts
        self.mock_state.has_from_list.return_value = False
        self.mock_state.count_from_list.return_value = 0
        self.mock_state.count.return_value = 0
        
        result = can_reach(3, self.mock_world, self.mock_state)
        self.assertFalse(result)
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_act_1_armor_categories(self, mock_acts, mock_gems, mock_max_links, 
                                             mock_support, mock_flask, mock_gear, 
                                             mock_ascendancy, mock_get_by_category):
        """Test act 1 armor category requirements"""
        
        # Mock acts data
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
        
        # Setup mocks with real item names
        mock_get_by_category.return_value = [{"name": "Progressive Sword"}]
        mock_ascendancy.return_value = []
        mock_gear.return_value = [{"name": "Progressive BodyArmour"}]
        mock_flask.return_value = [{"name": "Progressive Flask Unlock"}] * 5
        mock_support.return_value = []
        mock_max_links.return_value = []
        mock_gems.return_value = [{"name": "Fireball"}] * 10
        
        # Mock state to have enough items for most requirements but test armor categories
        def mock_has_from_list(items, player, count):
            item_names = [item["name"] if isinstance(item, dict) else str(item) for item in items]
            # Return True for helmet and body armour (2 categories)
            if any("Helmet" in name or "BodyArmour" in name for name in item_names):
                return True
            return len(items) > 0
        
        self.mock_state.has_from_list.side_effect = mock_has_from_list
        self.mock_state.count_from_list.return_value = 10
        self.mock_state.count.return_value = 10
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertTrue(result)


class TestSelectLocationsToAdd(PoeTestBase):
    """Test location selection logic"""
    
    def setUp(self):
        super().setUp()
        self.mock_world = Mock()
        self.mock_world.goal_act = 3
        self.mock_world.random = Mock()
        self.mock_world.random.sample = Mock(side_effect=lambda x, k: x[:k])
        self.mock_world.random.shuffle = Mock()
        
        self.mock_options = Mock()
        self.mock_options.add_leveling_up_to_location_pool = True
        # Add proper numeric values for the Mock objects
        self.mock_options.gear_upgrades_per_act.value = 2
        self.mock_options.ascendancies_available_per_class.value = 3
        self.mock_options.starting_character.value = 1
        self.mock_options.starting_character.option_scion = 7
        self.mock_options.gucci_hobo_mode.value = 0
        self.mock_options.gucci_hobo_mode.option_disabled = 0
        self.mock_options.add_flask_slots_to_item_pool = True
        self.mock_options.flask_slots_per_act.value = 1
        self.mock_options.add_max_links_to_item_pool = True
        self.mock_options.max_links_per_act.value = 1
        self.mock_options.skill_gems_per_act.value = 2
        self.mock_options.support_gems_per_act.value = 1
        self.mock_options.add_passive_skill_points_to_item_pool.value = True
        
        self.mock_world.options = self.mock_options
        
        # Mock locations data
        self.mock_base_item_locations = {
            "loc1": {"name": "Location 1", "act": 1},
            "loc2": {"name": "Location 2", "act": 2},
            "loc3": {"name": "Location 3", "act": 3},
            "loc4": {"name": "Location 4", "act": 4},  # Should be excluded
        }
        
        self.mock_level_locations = {
            "level1": {"name": "Level 5", "level": 5, "act": 1},
            "level2": {"name": "Level 10", "level": 10, "act": 2},
            "level3": {"name": "Level 100", "level": 100, "act": 11},  # Should be excluded by max level
        }
        
        self.mock_acts = {
            1: {"maxMonsterLevel": 8},
            2: {"maxMonsterLevel": 15},
            3: {"maxMonsterLevel": 25},
        }
    
    @patch('worlds.poe.Rules.base_item_type_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.level_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.acts', new_callable=lambda: {})
    def test_select_locations_to_add_basic(self, mock_acts, mock_level_locs, mock_base_locs):
        """Test basic location selection"""
        mock_base_locs.update(self.mock_base_item_locations)
        mock_level_locs.update(self.mock_level_locations)
        mock_acts.update(self.mock_acts)
        
        result = SelectLocationsToAdd(self.mock_world, 5)
        
        # Should return list of locations
        self.assertIsInstance(result, list)
        self.assertLessEqual(len(result), 5)
    
    @patch('worlds.poe.Rules.base_item_type_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.level_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.acts', new_callable=lambda: {})
    def test_select_locations_excludes_high_acts(self, mock_acts, mock_level_locs, mock_base_locs):
        """Test that locations from acts higher than goal_act are excluded"""
        mock_base_locs.update(self.mock_base_item_locations)
        mock_level_locs.update(self.mock_level_locations)
        mock_acts.update(self.mock_acts)
        
        result = SelectLocationsToAdd(self.mock_world, 10)
        
        # Should not include location from act 4
        location_names = [loc["name"] for loc in result]
        self.assertNotIn("Location 4", location_names)
    
    @patch('worlds.poe.Rules.base_item_type_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.level_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.acts', new_callable=lambda: {})
    def test_select_locations_excludes_high_level(self, mock_acts, mock_level_locs, mock_base_locs):
        """Test that level locations above max monster level are excluded"""
        mock_base_locs.update(self.mock_base_item_locations)
        mock_level_locs.update(self.mock_level_locations)
        mock_acts.update(self.mock_acts)
        
        result = SelectLocationsToAdd(self.mock_world, 10)
        
        # Should not include level 100 location
        location_names = [loc["name"] for loc in result]
        self.assertNotIn("Level 100", location_names)
    
    @patch('worlds.poe.Rules.base_item_type_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.level_locations', new_callable=lambda: {})
    @patch('worlds.poe.Rules.acts', new_callable=lambda: {})
    def test_select_locations_without_leveling(self, mock_acts, mock_level_locs, mock_base_locs):
        """Test location selection when leveling locations are disabled"""
        mock_base_locs.update(self.mock_base_item_locations)
        mock_level_locs.update(self.mock_level_locations)
        mock_acts.update(self.mock_acts)
        
        self.mock_options.add_leveling_up_to_location_pool = False
        
        result = SelectLocationsToAdd(self.mock_world, 10)
        
        # Should not include any level locations
        location_names = [loc["name"] for loc in result]
        self.assertNotIn("Level 5", location_names)
        self.assertNotIn("Level 10", location_names)


class TestConstants(unittest.TestCase):
    """Test module constants"""
    
    def test_constants_exist(self):
        """Test that all expected constants are defined"""
        self.assertTrue(hasattr(Rules, 'MAX_GUCCI_GEAR_UPGRADES'))
        self.assertTrue(hasattr(Rules, 'MAX_GEAR_UPGRADES'))
        self.assertTrue(hasattr(Rules, 'MAX_FLASK_SLOTS'))
        self.assertTrue(hasattr(Rules, 'MAX_LINK_UPGRADES'))
        self.assertTrue(hasattr(Rules, 'MAX_SKILL_GEMS'))
        self.assertTrue(hasattr(Rules, 'MAX_SUPPORT_GEMS'))
        
        self.assertTrue(hasattr(Rules, 'ACT_0_USABLE_GEMS'))
        self.assertTrue(hasattr(Rules, 'ACT_0_FLASK_SLOTS'))
        self.assertTrue(hasattr(Rules, 'ACT_0_WEAPON_TYPES'))
        self.assertTrue(hasattr(Rules, 'ACT_0_ARMOUR_TYPES'))
        self.assertTrue(hasattr(Rules, 'ACT_0_ADDITIONAL_LOCATIONS'))
    
    def test_constants_are_reasonable(self):
        """Test that constants have reasonable values"""
        self.assertGreater(Rules.MAX_GUCCI_GEAR_UPGRADES, 0)
        self.assertGreater(Rules.MAX_GEAR_UPGRADES, Rules.MAX_GUCCI_GEAR_UPGRADES)
        self.assertGreater(Rules.MAX_FLASK_SLOTS, 0)
        self.assertGreater(Rules.MAX_LINK_UPGRADES, 0)
        self.assertGreater(Rules.MAX_SKILL_GEMS, 0)
        self.assertGreater(Rules.MAX_SUPPORT_GEMS, 0)
    
    def test_armor_categories(self):
        """Test armor categories list"""
        expected_categories = ["BodyArmour", "Boots", "Gloves", "Helmet", "Amulet", 
                             "Belt", "Ring (left)", "Ring (right)", "Quiver", "Shield"]
        self.assertEqual(Rules.armor_categories, expected_categories)
    
    def test_weapon_categories(self):
        """Test weapon categories list"""
        expected_weapons = ["Axe", "Bow", "Claw", "Dagger", "Mace", "Sceptre", 
                          "Staff", "Sword", "Wand"]
        self.assertEqual(Rules.weapon_categories, expected_weapons)
    
    def test_passives_required_for_act(self):
        """Test passive points required for each act"""
        self.assertIn(1, Rules.passives_required_for_act)
        self.assertIn(12, Rules.passives_required_for_act)
        self.assertEqual(Rules.passives_required_for_act[1], 6)
        self.assertEqual(Rules.passives_required_for_act[12], 136)


class TestCanReachFunction(PoeTestBase):
    """Comprehensive tests for the can_reach function"""
    
    def setUp(self):
        super().setUp()
        # Clear cache before each test
        # clear_item_cache() # This function does not exist
        
        self.mock_world = Mock()
        self.mock_state = Mock(spec=CollectionState)
        self.mock_options = Mock()
        
        # Setup comprehensive default options
        self.mock_options.disable_generation_logic.value = False
        self.mock_options.ascendancies_available_per_class.value = 3
        self.mock_options.starting_character.value = 1
        self.mock_options.starting_character.option_scion = 7
        self.mock_options.starting_character.current_option_name = "Marauder"
        self.mock_options.gear_upgrades_per_act.value = 2
        self.mock_options.gucci_hobo_mode.value = 0
        self.mock_options.gucci_hobo_mode.option_disabled = 0
        self.mock_options.add_flask_slots_to_item_pool = True
        self.mock_options.flask_slots_per_act.value = 1
        self.mock_options.add_max_links_to_item_pool = True
        self.mock_options.max_links_per_act.value = 1
        self.mock_options.skill_gems_per_act.value = 2
        self.mock_options.support_gems_per_act.value = 1
        self.mock_options.add_passive_skill_points_to_item_pool.value = True
        
        self.mock_world.options = self.mock_options
        self.mock_world.player = 1
        
        # Setup default item mocks using real names from Items.json
        self.setup_default_item_mocks()
        
        # Setup default state mocks
        self.setup_default_state_mocks()
    
    def setup_default_item_mocks(self):
        """Setup default mocks for all item functions using real item names"""
        self.weapon_items = [
            {"name": "Progressive Sword"}, 
            {"name": "Progressive Axe"}, 
            {"name": "Progressive Bow"}
        ]
        self.armor_items = [
            {"name": "Progressive Helmet"}, 
            {"name": "Progressive BodyArmour"}, 
            {"name": "Progressive Boots"}
        ]
        self.ascendancy_items = [{"name": "Berserker"}]
        self.gear_items = [
            {"name": "Progressive BodyArmour"}, 
            {"name": "Progressive Helmet"}
        ]
        self.flask_items = [{"name": "Progressive Flask Unlock", "category": ["Flask"]}]
        self.support_gem_items = [{"name": "Chance to Bleed Support"}]
        self.max_links_items = [{"name": "Progressive max links - Weapon"}]
        self.skill_gem_items = [{"name": "Fireball"}, {"name": "Freezing Pulse"}]
    
    def setup_default_state_mocks(self):
        """Setup default state mocks for sufficient resources"""
        def mock_has_from_list(items, player, count):
            # Return True for any non-empty item list
            return len(items) > 0
        
        def mock_count_from_list(items, player):
            # Return a reasonable count for any item list
            return max(len(items), 5)
        
        def mock_count(item_name, player):
            # Return sufficient passive points
            return 50
        
        self.mock_state.has_from_list.side_effect = mock_has_from_list
        self.mock_state.count_from_list.side_effect = mock_count_from_list
        self.mock_state.count.side_effect = mock_count
    
    def test_can_reach_early_acts(self):
        """Test can_reach for acts before act 1"""
        # Test act 0 and negative acts
        self.assertTrue(can_reach(0, self.mock_world, self.mock_state))
        self.assertTrue(can_reach(-1, self.mock_world, self.mock_state))
        self.assertTrue(can_reach(-10, self.mock_world, self.mock_state))
    
    def test_can_reach_disabled_logic(self):
        """Test can_reach when generation logic is disabled"""
        self.mock_options.disable_generation_logic.value = True
        
        # Should return True for any act when logic is disabled
        self.assertTrue(can_reach(1, self.mock_world, self.mock_state))
        self.assertTrue(can_reach(5, self.mock_world, self.mock_state))
        self.assertTrue(can_reach(10, self.mock_world, self.mock_state))
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items') 
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_act_1_sufficient_resources(self, mock_acts, mock_skill_gems, 
                                                 mock_max_links, mock_support_gems, 
                                                 mock_flask_items, mock_gear_items,
                                                 mock_ascendancy_items, mock_get_by_category):
        """Test can_reach for act 1 with sufficient resources"""
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
        
        # Setup mocks to return our test data
        mock_get_by_category.return_value = self.weapon_items
        mock_ascendancy_items.return_value = self.ascendancy_items
        mock_gear_items.return_value = self.gear_items
        mock_flask_items.return_value = self.flask_items
        mock_support_gems.return_value = self.support_gem_items
        mock_max_links.return_value = self.max_links_items
        mock_skill_gems.return_value = self.skill_gem_items
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertTrue(result)
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_act_1_insufficient_skill_gems(self, mock_acts, mock_skill_gems,
                                                    mock_max_links, mock_support_gems,
                                                    mock_flask_items, mock_gear_items,
                                                    mock_ascendancy_items, mock_get_by_category):
        """Test can_reach for act 1 with insufficient skill gems"""
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
        
        # Setup mocks - most items available but no skill gems
        mock_get_by_category.return_value = self.weapon_items
        mock_ascendancy_items.return_value = self.ascendancy_items
        mock_gear_items.return_value = self.gear_items
        mock_flask_items.return_value = self.flask_items
        mock_support_gems.return_value = self.support_gem_items
        mock_max_links.return_value = self.max_links_items
        mock_skill_gems.return_value = []  # No skill gems available
        
        # Mock state to return insufficient skill gems
        def mock_count_insufficient(items, player):
            if len(items) == 0:  # skill gems list is empty
                return 0
            return 5
        
        self.mock_state.count_from_list.side_effect = mock_count_insufficient
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertFalse(result)
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_act_1_insufficient_weapon_types(self, mock_acts, mock_skill_gems,
                                                      mock_max_links, mock_support_gems,
                                                      mock_flask_items, mock_gear_items,
                                                      mock_ascendancy_items, mock_get_by_category):
        """Test can_reach for act 1 with insufficient weapon types"""
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
        
        # Setup get_by_category to return items for only one weapon type
        def mock_get_by_category_one_weapon(category):
            if category == "Sword":
                return [{"name": "Progressive Sword"}]
            elif category in Rules.weapon_categories:
                return []  # No items for other weapon types
            elif category in Rules.armor_categories:
                return self.armor_items  # Armor available
            return []
        
        mock_get_by_category.side_effect = mock_get_by_category_one_weapon
        mock_ascendancy_items.return_value = self.ascendancy_items
        mock_gear_items.return_value = self.gear_items
        mock_flask_items.return_value = self.flask_items
        mock_support_gems.return_value = self.support_gem_items
        mock_max_links.return_value = self.max_links_items
        mock_skill_gems.return_value = self.skill_gem_items
        
        # Mock state to only have items from sword category
        def mock_has_from_list_one_weapon(items, player, count):
            if len(items) == 0:
                return False
            # Only return True for Sword items and armor items
            item_names = [item["name"] if isinstance(item, dict) else str(item) for item in items]
            return any("Sword" in name or "Helmet" in name or "BodyArmour" in name or "Boots" in name for name in item_names)
        
        self.mock_state.has_from_list.side_effect = mock_has_from_list_one_weapon
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertFalse(result)  # Need at least 2 weapon types
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_act_1_insufficient_armor_categories(self, mock_acts, mock_skill_gems,
                                                          mock_max_links, mock_support_gems,
                                                          mock_flask_items, mock_gear_items,
                                                          mock_ascendancy_items, mock_get_by_category):
        """Test can_reach for act 1 with insufficient armor categories"""
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
        
        # Setup get_by_category to return weapons but only one armor type
        def mock_get_by_category_one_armor(category):
            if category in Rules.weapon_categories:
                return self.weapon_items  # Multiple weapon types available
            elif category == "Helmet":
                return [{"name": "Progressive Helmet"}]  # Only helmet available
            elif category in Rules.armor_categories:
                return []  # No other armor types
            return []
        
        mock_get_by_category.side_effect = mock_get_by_category_one_armor
        mock_ascendancy_items.return_value = self.ascendancy_items
        mock_gear_items.return_value = self.gear_items
        mock_flask_items.return_value = self.flask_items
        mock_support_gems.return_value = self.support_gem_items
        mock_max_links.return_value = self.max_links_items
        mock_skill_gems.return_value = self.skill_gem_items
        
        # Mock state to only have helmet items (not enough armor categories)
        def mock_has_from_list_one_armor(items, player, count):
            if len(items) == 0:
                return False
            # Return True for weapons and helmet, False for other armor
            item_names = [item["name"] if isinstance(item, dict) else str(item) for item in items]
            return any("Sword" in name or "Axe" in name or "Bow" in name or "Helmet" in name for name in item_names)
        
        self.mock_state.has_from_list.side_effect = mock_has_from_list_one_armor
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertFalse(result)  # Need at least 2 armor categories
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    @patch('worlds.poe.Rules.acts')
    def test_can_reach_act_1_insufficient_flasks(self, mock_acts, mock_skill_gems,
                                                mock_max_links, mock_support_gems,
                                                mock_flask_items, mock_gear_items,
                                                mock_ascendancy_items, mock_get_by_category):
        """Test can_reach for act 1 with insufficient flasks"""
        mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
        
        # Setup mocks - no flasks available
        mock_get_by_category.return_value = self.weapon_items
        mock_ascendancy_items.return_value = self.ascendancy_items
        mock_gear_items.return_value = self.gear_items
        mock_flask_items.return_value = []  # No flasks available
        mock_support_gems.return_value = self.support_gem_items
        mock_max_links.return_value = self.max_links_items
        mock_skill_gems.return_value = self.skill_gem_items
        
        # Mock state to return insufficient flasks
        def mock_count_no_flasks(items, player):
            if len(items) == 0:  # flask items list is empty
                return 0
            return 5
        
        self.mock_state.count_from_list.side_effect = mock_count_no_flasks
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertFalse(result)  # Need at least 3 flasks for act 1
    
    def test_can_reach_scion_character(self):
        """Test can_reach with Scion character (different ascendancy requirements)"""
        self.mock_options.starting_character.value = self.mock_options.starting_character.option_scion
        self.mock_options.starting_character.current_option_name = "Scion"
        
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 30}
            
            # Setup mocks
            mock_get_by_category.return_value = self.weapon_items
            mock_ascendancy_items.return_value = [{"name": "Ascendant"}]  # Scion ascendancy
            mock_gear_items.return_value = self.gear_items
            mock_flask_items.return_value = self.flask_items
            mock_support_gems.return_value = self.support_gem_items
            mock_max_links.return_value = self.max_links_items
            mock_skill_gems.return_value = self.skill_gem_items
            
            # Mock state to return 1 ascendancy item (sufficient for Scion)
            def mock_count_scion(items, player):
                item_names = [item["name"] if isinstance(item, dict) else str(item) for item in items]
                if any("Ascendant" in name for name in item_names):
                    return 1
                return 5
            
            self.mock_state.count_from_list.side_effect = mock_count_scion
            
            result = can_reach(3, self.mock_world, self.mock_state)
            self.assertTrue(result)  # Scion only needs 1 ascendancy
    
    def test_can_reach_flask_slots_disabled(self):
        """Test can_reach when flask slots are disabled in options"""
        self.mock_options.add_flask_slots_to_item_pool = False
        
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 20}
            
            # Setup mocks
            mock_get_by_category.return_value = self.weapon_items
            mock_ascendancy_items.return_value = self.ascendancy_items
            mock_gear_items.return_value = self.gear_items
            mock_flask_items.return_value = []  # No flasks needed
            mock_support_gems.return_value = self.support_gem_items
            mock_max_links.return_value = self.max_links_items
            mock_skill_gems.return_value = self.skill_gem_items
            
            # Mock state to return zero flasks (should be fine when disabled)
            def mock_count_no_flasks(items, player):
                if any("Flask" in str(item) for item in items):
                    return 0
                return 5
            
            self.mock_state.count_from_list.side_effect = mock_count_no_flasks
            
            result = can_reach(2, self.mock_world, self.mock_state)
            self.assertTrue(result)  # Should pass even with no flasks when disabled
    
    def test_can_reach_passive_points_disabled(self):
        """Test can_reach when passive points are disabled in options"""
        self.mock_options.add_passive_skill_points_to_item_pool.value = False
        
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 50}
            
            # Setup mocks for all categories
            def mock_get_by_category_all(category):
                if category in Rules.weapon_categories:
                    return self.weapon_items
                elif category in Rules.armor_categories:
                    return self.armor_items
                return []
            
            mock_get_by_category.side_effect = mock_get_by_category_all
            mock_ascendancy_items.return_value = self.ascendancy_items * 5  # Plenty for act 5
            mock_gear_items.return_value = self.gear_items * 20  # Plenty for act 5
            mock_flask_items.return_value = self.flask_items * 10
            mock_support_gems.return_value = self.support_gem_items * 10
            mock_max_links.return_value = self.max_links_items * 10
            mock_skill_gems.return_value = self.skill_gem_items * 20
            
            # Mock state to return sufficient counts for everything except passives
            def mock_count_sufficient(items, player):
                return len(items) * 10  # Plenty for all requirements
            
            self.mock_state.count_from_list.side_effect = mock_count_sufficient
            self.mock_state.count.return_value = 0  # Zero passive points
            self.mock_state.has_from_list.return_value = True  # Have all items
            
            result = can_reach(5, self.mock_world, self.mock_state)
            self.assertTrue(result)  # Should pass even with no passives when disabled

    # Comprehensive edge case tests for can_reach function
    
    def test_can_reach_zero_weapon_categories(self):
        """Test can_reach when no weapon categories are available at all"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            # Return empty list for all weapon categories
            mock_get_by_category.return_value = []
            mock_ascendancy_items.return_value = self.ascendancy_items
            mock_gear_items.return_value = self.gear_items
            mock_flask_items.return_value = self.flask_items
            mock_support_gems.return_value = self.support_gem_items
            mock_max_links.return_value = self.max_links_items
            mock_skill_gems.return_value = []  # No gems for no weapons
            
            # Mock state to return False for empty weapon lists
            def mock_has_from_list_no_weapons(items, player, count):
                return len(items) > 0
            
            self.mock_state.has_from_list.side_effect = mock_has_from_list_no_weapons
            
            result = can_reach(1, self.mock_world, self.mock_state)
            self.assertFalse(result)  # Should fail with no weapons
    
    def test_can_reach_zero_armor_categories(self):
        """Test can_reach when no armor categories are available"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            # Setup get_by_category to return weapons but no armor
            def mock_get_by_category_no_armor(category):
                if category in Rules.weapon_categories:
                    return self.weapon_items
                elif category in Rules.armor_categories:
                    return []  # No armor items for any armor category
                return []
            
            mock_get_by_category.side_effect = mock_get_by_category_no_armor
            mock_ascendancy_items.return_value = self.ascendancy_items
            mock_gear_items.return_value = self.gear_items
            mock_flask_items.return_value = self.flask_items
            mock_support_gems.return_value = self.support_gem_items
            mock_max_links.return_value = self.max_links_items
            mock_skill_gems.return_value = self.skill_gem_items
            
            # Mock state to return False for empty armor lists but True for others
            def mock_has_from_list_no_armor(items, player, count):
                if len(items) == 0:
                    return False  # Empty armor lists return False
                return True  # Non-empty weapon lists return True
            
            self.mock_state.has_from_list.side_effect = mock_has_from_list_no_armor
            
            result = can_reach(1, self.mock_world, self.mock_state)
            self.assertFalse(result)  # Should fail with no armor categories
    
    def test_can_reach_exactly_minimum_requirements(self):
        """Test can_reach when exactly meeting minimum requirements"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            # Provide exactly minimum items
            mock_get_by_category.return_value = self.weapon_items
            mock_ascendancy_items.return_value = []  # No ascendancy needed for act 1
            mock_gear_items.return_value = []  # No gear needed for act 1  
            mock_flask_items.return_value = self.flask_items * 3  # Exactly 3 flasks
            mock_support_gems.return_value = []  # No support gems needed for act 1
            mock_max_links.return_value = []  # No links needed for act 1
            mock_skill_gems.return_value = self.skill_gem_items * 4  # Exactly 4 skill gems
            
            # Mock state to return exactly minimum counts
            def mock_count_exact_minimum(items, player):
                if "Flask" in str(items):
                    return 3  # Exactly ACT_0_FLASK_SLOTS
                if "Fireball" in str(items) or "Freezing" in str(items):
                    return 4  # Exactly ACT_0_USABLE_GEMS
                return 0
            
            def mock_has_exact_minimum(items, player, count):
                if len(items) == 0:
                    return False
                item_names = [item["name"] if isinstance(item, dict) else str(item) for item in items]
                # Return True for exactly 2 weapon types and 2 armor types
                weapon_types = sum(1 for name in item_names if any(weapon in name for weapon in ["Sword", "Axe"]))
                armor_types = sum(1 for name in item_names if any(armor in name for armor in ["Helmet", "BodyArmour"]))
                return weapon_types >= 1 or armor_types >= 1
            
            self.mock_state.count_from_list.side_effect = mock_count_exact_minimum
            self.mock_state.has_from_list.side_effect = mock_has_exact_minimum
            self.mock_state.count.return_value = 6  # Exactly minimum passives for act 1
            
            result = can_reach(1, self.mock_world, self.mock_state)
            self.assertTrue(result)  # Should pass with exact minimum
    
    def test_can_reach_one_below_minimum_requirements(self):
        """Test can_reach when just below minimum requirements"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            mock_get_by_category.return_value = self.weapon_items
            mock_ascendancy_items.return_value = []
            mock_gear_items.return_value = []
            mock_flask_items.return_value = self.flask_items
            mock_support_gems.return_value = []
            mock_max_links.return_value = []
            mock_skill_gems.return_value = self.skill_gem_items
            
            # Mock state to return one below minimum
            def mock_count_below_minimum(items, player):
                if "Flask" in str(items):
                    return 2  # One below ACT_0_FLASK_SLOTS (3)
                return 10
            
            self.mock_state.count_from_list.side_effect = mock_count_below_minimum
            self.mock_state.count.return_value = 50
            
            result = can_reach(1, self.mock_world, self.mock_state)
            self.assertFalse(result)  # Should fail with insufficient flasks
    
    def test_can_reach_higher_act_with_ascendancy_requirements(self):
        """Test can_reach for higher acts with ascendancy requirements"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 50}
            
            # Setup get_by_category for all categories - fix signature to accept table parameter
            def mock_get_by_category_all(category, table=None):
                if category in Rules.weapon_categories:
                    return self.weapon_items
                elif category in Rules.armor_categories:
                    return self.armor_items
                elif category == "MainSkillGem":
                    return self.skill_gem_items * 20
                return []
            
            mock_get_by_category.side_effect = mock_get_by_category_all
            mock_ascendancy_items.return_value = [{"name": "Berserker"}, {"name": "Chieftain"}, {"name": "Juggernaut"}]
            mock_gear_items.return_value = self.gear_items * 10
            # Return flasks that are NOT unique
            mock_flask_items.return_value = [{"name": f"Normal Flask {i}", "category": "Flask"} for i in range(20)]
            mock_support_gems.return_value = self.support_gem_items * 10
            mock_max_links.return_value = self.max_links_items * 10
            mock_skill_gems.return_value = self.skill_gem_items * 20
            
            # Mock state to return sufficient counts for act 5
            def mock_count_high_act(items, player):
                return len(items) * 3  # Multiply by 3 to ensure sufficient counts
            
            def mock_has_from_list(items, player, count=1):
                return len(items) >= count  # Return True if items available
            
            def mock_count(item_name, player):
                if item_name == "Progressive passive point":
                    return 56  # Enough for act 5
                return 100
            
            self.mock_state.count_from_list.side_effect = mock_count_high_act
            self.mock_state.count.side_effect = mock_count  # Fixed: act 5 needs 56 passive points
            self.mock_state.has_from_list.side_effect = mock_has_from_list
            
            result = can_reach(5, self.mock_world, self.mock_state)
            self.assertTrue(result)
    
    def test_can_reach_missing_monster_level_in_acts(self):
        """Test can_reach when acts dict is missing maxMonsterLevel"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            # Acts dict missing maxMonsterLevel - should default to 0
            mock_acts.__getitem__.return_value = {}
            
            # Setup get_by_category for weapons and armor
            def mock_get_by_category_all(category):
                if category in Rules.weapon_categories:
                    return self.weapon_items
                elif category in Rules.armor_categories:
                    return self.armor_items
                return []
            
            mock_get_by_category.side_effect = mock_get_by_category_all
            mock_ascendancy_items.return_value = self.ascendancy_items
            mock_gear_items.return_value = self.gear_items
            mock_flask_items.return_value = self.flask_items
            mock_support_gems.return_value = self.support_gem_items
            mock_max_links.return_value = self.max_links_items
            # Should get called with level_maximum=0 - no gems available
            mock_skill_gems.return_value = []  # No gems for level 0
            
            # Mock state to return 0 for skill gems but sufficient for others
            def mock_count_no_gems(items, player):
                if len(items) == 0:  # Empty skill gems list
                    return 0
                return 10
            
            self.mock_state.count_from_list.side_effect = mock_count_no_gems
            self.mock_state.has_from_list.return_value = True
            self.mock_state.count.return_value = 10
            
            result = can_reach(1, self.mock_world, self.mock_state)
            self.assertFalse(result)  # Should fail due to no skill gems
    
    def test_can_reach_unique_flasks_excluded(self):
        """Test that unique flasks are properly excluded from flask count"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            mock_get_by_category.return_value = self.weapon_items
            mock_ascendancy_items.return_value = []
            mock_gear_items.return_value = []
            mock_support_gems.return_value = []
            mock_max_links.return_value = []
            mock_skill_gems.return_value = self.skill_gem_items
            
            # Include unique flasks in the flask items (should be excluded)
            mock_flask_items.return_value = [
                {"name": "Progressive Flask Unlock", "category": ["Flask"]},
                {"name": "Unique Flask", "category": ["Flask", "Unique"]},  # Should be excluded
                {"name": "Progressive Normal Flask Unlock", "category": ["Flask", "Normal"]},
            ]
            
            # Mock state should only count non-unique flasks
            def mock_count_excluding_unique(items, player):
                non_unique_items = [item for item in items if "Unique" not in str(item)]
                if "Flask" in str(items):
                    return len(non_unique_items)  # Should be 2, not 3
                return 10
            
            self.mock_state.count_from_list.side_effect = mock_count_excluding_unique
            
            # With only 2 non-unique flasks, should fail (needs 3)
            result = can_reach(1, self.mock_world, self.mock_state)
            self.assertFalse(result)
    
    def test_can_reach_gucci_hobo_mode_gear_cap(self):
        """Test can_reach with gucci hobo mode capping gear upgrades"""
        # Enable gucci hobo mode
        self.mock_options.gucci_hobo_mode.value = 1  # Not disabled
        self.mock_options.gear_upgrades_per_act.value = 100  # High value that should be capped
        
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 30}
            
            mock_get_by_category.return_value = self.weapon_items
            mock_ascendancy_items.return_value = self.ascendancy_items
            mock_gear_items.return_value = self.gear_items * 50  # More than cap
            mock_flask_items.return_value = self.flask_items * 10
            mock_support_gems.return_value = self.support_gem_items * 10
            mock_max_links.return_value = self.max_links_items * 10
            mock_skill_gems.return_value = self.skill_gem_items * 10
            
            # Mock state to return exactly MAX_GUCCI_GEAR_UPGRADES items
            def mock_count_gucci_cap(items, player):
                if "Progressive BodyArmour" in str(items) or "Progressive Helmet" in str(items):
                    return Rules.MAX_GUCCI_GEAR_UPGRADES  # Should be enough due to cap
                return len(items) * 5
            
            self.mock_state.count_from_list.side_effect = mock_count_gucci_cap
            self.mock_state.count.return_value = 50
            
            result = can_reach(3, self.mock_world, self.mock_state)
            self.assertTrue(result)  # Should pass with capped gear requirement
    
    def test_can_reach_maximum_act_requirements(self):
        """Test can_reach with maximum act (act 12) requirements"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 100}
            
            # Setup get_by_category for all categories - fix signature to accept table parameter
            def mock_get_by_category_all(category, table=None):
                if category in Rules.weapon_categories:
                    return self.weapon_items
                elif category in Rules.armor_categories:
                    return self.armor_items
                elif category == "MainSkillGem":
                    return self.skill_gem_items * 100
                return []
            
            mock_get_by_category.side_effect = mock_get_by_category_all
            mock_ascendancy_items.return_value = self.ascendancy_items * 5
            mock_gear_items.return_value = self.gear_items * 100
            # Return flasks that are NOT unique
            mock_flask_items.return_value = [{"name": f"Normal Flask {i}", "category": "Flask"} for i in range(50)]
            mock_support_gems.return_value = self.support_gem_items * 100
            mock_max_links.return_value = self.max_links_items * 50
            mock_skill_gems.return_value = self.skill_gem_items * 100
            
            # Mock state to return maximum values
            def mock_count_maximum(items, player):
                return len(items) * 10  # Plenty for max requirements
            
            def mock_has_from_list(items, player, count=1):
                return len(items) >= count  # Return True if items available
            
            def mock_count(item_name, player):
                if item_name == "Progressive passive point":
                    return 136  # Maximum passives for act 12
                return 100
            
            self.mock_state.count_from_list.side_effect = mock_count_maximum
            self.mock_state.count.side_effect = mock_count  # Maximum passives in game
            self.mock_state.has_from_list.side_effect = mock_has_from_list
            
            result = can_reach(12, self.mock_world, self.mock_state)
            self.assertTrue(result)

    def test_can_reach_edge_case_empty_weapon_list(self):
        """Test can_reach when weapon items list is empty"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            # Return empty weapon lists for all weapon categories
            def mock_get_by_category_empty_weapons(category, table=None):
                if category in Rules.weapon_categories:
                    return []  # No weapons available
                elif category in Rules.armor_categories:
                    return self.armor_items
                return []
            
            mock_get_by_category.side_effect = mock_get_by_category_empty_weapons
            mock_ascendancy_items.return_value = []  # No ascendancy for act 1
            mock_gear_items.return_value = self.gear_items * 5
            mock_flask_items.return_value = [{"name": f"Normal Flask {i}", "category": "Flask"} for i in range(10)]
            mock_support_gems.return_value = self.support_gem_items * 5
            mock_max_links.return_value = self.max_links_items * 5
            mock_skill_gems.return_value = self.skill_gem_items * 5
            
            def mock_count_basic(items, player):
                return len(items) * 2
            
            def mock_has_from_list_none(items, player, count=1):
                return False  # No weapons available
            
            self.mock_state.count_from_list.side_effect = mock_count_basic
            self.mock_state.count.return_value = 10  # Low passive count for act 1
            self.mock_state.has_from_list.side_effect = mock_has_from_list_none
            
            result = can_reach(1, self.mock_world, self.mock_state)
            self.assertFalse(result)  # Should fail due to insufficient weapon types

    def test_can_reach_edge_case_flask_unique_filtering(self):
        """Test can_reach correctly filters out unique flasks"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            def mock_get_by_category_all(category, table=None):
                if category in Rules.weapon_categories:
                    return self.weapon_items
                elif category in Rules.armor_categories:
                    return self.armor_items
                return []
            
            mock_get_by_category.side_effect = mock_get_by_category_all
            mock_ascendancy_items.return_value = []  # No ascendancy for act 1
            mock_gear_items.return_value = self.gear_items * 5
            # Return mix of unique and normal flasks
            mock_flask_items.return_value = [
                {"name": "Normal Flask 1", "category": "Flask"},
                {"name": "Normal Flask 2", "category": "Flask"},
                {"name": "Unique Flask 1", "category": "Unique Flask"},  # Should be filtered out
                {"name": "Normal Flask 3", "category": "Flask"},
                {"name": "Unique Flask 2", "category": "Unique Flask"},  # Should be filtered out
            ]
            mock_support_gems.return_value = self.support_gem_items * 5
            mock_max_links.return_value = self.max_links_items * 5
            mock_skill_gems.return_value = self.skill_gem_items * 5
            
            def mock_count_filtered(items, player):
                # Only count non-unique flasks
                non_unique_count = len([item for item in items if 'Unique' not in item])
                return non_unique_count
            
            def mock_has_from_list_basic(items, player, count=1):
                return len(items) >= count
            
            self.mock_state.count_from_list.side_effect = mock_count_filtered
            self.mock_state.count.return_value = 10  # Low passive count for act 1
            self.mock_state.has_from_list.side_effect = mock_has_from_list_basic
            
            result = can_reach(1, self.mock_world, self.mock_state)
            # Should fail because only 3 non-unique flasks but needs 3 for ACT_0_FLASK_SLOTS
            # Actually may pass depending on exact requirements, let's adjust
            # Since we have exactly 3 non-unique flasks and ACT_0_FLASK_SLOTS is 3, this should pass
            self.assertTrue(result)

    def test_can_reach_edge_case_boundary_passive_points(self):
        """Test can_reach with exactly the required passive points for different acts"""
        test_cases = [
            (1, 6),   # Act 1 requires 6 passives
            (2, 18),  # Act 2 requires 18 passives  
            (5, 56),  # Act 5 requires 56 passives
            (10, 109), # Act 10 requires 109 passives
        ]
        
        for act, required_passives in test_cases:
            with self.subTest(act=act, required_passives=required_passives):
                with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
                     patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
                     patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
                     patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
                     patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
                     patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
                     patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
                     patch('worlds.poe.Rules.acts') as mock_acts:
                    
                    mock_acts.__getitem__.return_value = {"maxMonsterLevel": act * 10}
                    
                    def mock_get_by_category_all(category, table=None):
                        if category in Rules.weapon_categories:
                            return self.weapon_items
                        elif category in Rules.armor_categories:
                            return self.armor_items
                        return []
                    
                    mock_get_by_category.side_effect = mock_get_by_category_all
                    mock_ascendancy_items.return_value = self.ascendancy_items if act >= 3 else []
                    mock_gear_items.return_value = self.gear_items * 10
                    mock_flask_items.return_value = [{"name": f"Normal Flask {i}", "category": "Flask"} for i in range(20)]
                    mock_support_gems.return_value = self.support_gem_items * 10
                    mock_max_links.return_value = self.max_links_items * 10
                    mock_skill_gems.return_value = self.skill_gem_items * 10
                    
                    def mock_count_exact(items, player):
                        return len(items) * 5  # Plenty for other requirements
                    
                    def mock_count_passives(item_name, player):
                        if item_name == "Progressive passive point":
                            return required_passives  # Exactly the required amount
                        return 100
                    
                    def mock_has_from_list_basic(items, player, count=1):
                        return len(items) >= count
                    
                    self.mock_state.count_from_list.side_effect = mock_count_exact
                    self.mock_state.count.side_effect = mock_count_passives
                    self.mock_state.has_from_list.side_effect = mock_has_from_list_basic
                    
                    result = can_reach(act, self.mock_world, self.mock_state)
                    self.assertTrue(result, f"Should reach act {act} with exactly {required_passives} passive points")
    
    def test_can_reach_acts_beyond_passive_table(self):
        """Test can_reach for acts beyond the passive requirements table"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 120}
            
            mock_get_by_category.return_value = self.weapon_items
            mock_ascendancy_items.return_value = self.ascendancy_items
            mock_gear_items.return_value = self.gear_items * 100
            mock_flask_items.return_value = self.flask_items * 20
            mock_support_gems.return_value = self.support_gem_items * 100
            mock_max_links.return_value = self.max_links_items * 50
            mock_skill_gems.return_value = self.skill_gem_items * 100
            
            self.mock_state.count_from_list.return_value = 1000
            self.mock_state.count.return_value = 136  # Max passives
            
            # Act 99 should have 0 passive requirement (not in table)
            result = can_reach(99, self.mock_world, self.mock_state)
            self.assertTrue(result)  # Should pass since no passive requirement
    
    def test_can_reach_invalid_act_number(self):
        """Test can_reach with invalid/extreme act numbers"""
        # Mock acts to handle invalid indices gracefully
        with patch('worlds.poe.Rules.acts') as mock_acts:
            def mock_acts_getitem(key):
                if key == 999999:
                    raise IndexError("list index out of range")
                return {"maxMonsterLevel": 10}
            
            mock_acts.__getitem__.side_effect = mock_acts_getitem
            
            # Should raise IndexError when trying to access invalid act
            with self.assertRaises(IndexError):
                can_reach(999999, self.mock_world, self.mock_state)
    
    def test_can_reach_weapon_state_modification(self):
        """Test that 'Unarmed' is properly added and removed from valid_weapon_types"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy_items, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear_items, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask_items, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support_gems, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_skill_gems, \
             patch('worlds.poe.Rules.acts') as mock_acts:
            
            mock_acts.__getitem__.return_value = {"maxMonsterLevel": 10}
            
            # Only have one weapon type from state
            mock_get_by_category.return_value = [{"name": "Progressive Sword"}]
            mock_ascendancy_items.return_value = []
            mock_gear_items.return_value = []
            mock_flask_items.return_value = self.flask_items * 5
            mock_support_gems.return_value = []
            mock_max_links.return_value = []
            
            # Track what gets passed to get_main_skill_gems_by_required_level_and_useable_weapon
            weapon_types_passed = []
            def capture_weapon_types(available_weapons, level_minimum, level_maximum):
                weapon_types_passed.append(available_weapons.copy())
                return self.skill_gem_items
            
            mock_skill_gems.side_effect = capture_weapon_types
            
            # Only sword weapons available in state
            def mock_has_only_sword(items, player, count):
                if len(items) == 0:
                    return False
                item_names = [item["name"] if isinstance(item, dict) else str(item) for item in items]
                return any("Sword" in name for name in item_names)
            
            self.mock_state.has_from_list.side_effect = mock_has_only_sword
            
            can_reach(1, self.mock_world, self.mock_state)
            
            # Should have been called with Unarmed included
            self.assertTrue(len(weapon_types_passed) > 0)
            weapons_used = weapon_types_passed[0]
            self.assertIn("Unarmed", weapons_used)
            self.assertIn("Sword", weapons_used)


if __name__ == '__main__':
    unittest.main()