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
    def test_can_reach_act_1_requirements(self, mock_gems_by_weapon, mock_max_links, 
                                         mock_support_gems, mock_flask_items, 
                                         mock_gear_items, mock_ascendancy_items, 
                                         mock_get_by_category):
        """Test can_reach for act 1 with specific requirements"""
        
        # Mock item returns
        mock_weapon_items = [{"name": "Sword"}, {"name": "Axe"}, {"name": "Bow"}]
        mock_get_by_category.return_value = mock_weapon_items
        mock_ascendancy_items.return_value = []
        mock_gear_items.return_value = []
        mock_flask_items.return_value = []
        mock_support_gems.return_value = []
        mock_max_links.return_value = []
        mock_gems_by_weapon.return_value = [
            {"name": "Fireball"}, {"name": "Ice Bolt"}, 
            {"name": "Lightning Bolt"}, {"name": "Frost Bolt"}
        ]
        
        # Mock state counts
        self.mock_state.has_from_list.return_value = True
        self.mock_state.count_from_list.return_value = 5
        self.mock_state.count.return_value = 10
        
        result = can_reach(1, self.mock_world, self.mock_state)
        self.assertTrue(result)
    
    @patch('worlds.poe.Items.get_by_category')
    @patch('worlds.poe.Items.get_ascendancy_class_items')
    @patch('worlds.poe.Items.get_gear_items')
    @patch('worlds.poe.Items.get_flask_items')
    @patch('worlds.poe.Items.get_support_gem_items')
    @patch('worlds.poe.Items.get_max_links_items')
    @patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon')
    def test_can_reach_insufficient_requirements(self, mock_gems_by_weapon, mock_max_links,
                                                mock_support_gems, mock_flask_items,
                                                mock_gear_items, mock_ascendancy_items,
                                                mock_get_by_category):
        """Test can_reach when requirements are not met"""
        
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
    
    def test_can_reach_act_1_armor_categories(self):
        """Test act 1 armor category requirements"""
        with patch('worlds.poe.Items.get_by_category') as mock_get_by_category, \
             patch('worlds.poe.Items.get_ascendancy_class_items') as mock_ascendancy, \
             patch('worlds.poe.Items.get_gear_items') as mock_gear, \
             patch('worlds.poe.Items.get_flask_items') as mock_flask, \
             patch('worlds.poe.Items.get_support_gem_items') as mock_support, \
             patch('worlds.poe.Items.get_max_links_items') as mock_max_links, \
             patch('worlds.poe.Items.get_main_skill_gems_by_required_level_and_useable_weapon') as mock_gems:
            
            # Setup mocks
            mock_get_by_category.return_value = [{"name": "Sword"}]
            mock_ascendancy.return_value = []
            mock_gear.return_value = []
            mock_flask.return_value = []
            mock_support.return_value = []
            mock_max_links.return_value = []
            mock_gems.return_value = [{"name": "Fireball"}] * 10
            
            # Mock state to have enough items for most requirements but test armor categories
            def mock_has_from_list(items, player, count):
                if "Helmet" in str(items) or "BodyArmour" in str(items):
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


if __name__ == '__main__':
    unittest.main()
