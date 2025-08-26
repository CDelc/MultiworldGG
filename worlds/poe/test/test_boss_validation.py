import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add vendor libraries to path for dependencies like pygetwindow
current_dir = os.path.dirname(__file__)
poe_dir = os.path.dirname(current_dir)
worlds_dir = os.path.dirname(poe_dir)
archipelago_dir = os.path.dirname(worlds_dir)
poe_client_vendor_dir = os.path.join(archipelago_dir, "lib", "poe_client_vendor")

if poe_client_vendor_dir not in sys.path:
    sys.path.insert(0, poe_client_vendor_dir)


try:
    from . import PoeTestBase
    from ..poeClient import validationLogic
except ImportError:
    import sys
    import os
    
    current_dir = os.path.dirname(__file__)
    poe_dir = os.path.dirname(current_dir)
    worlds_dir = os.path.dirname(poe_dir)
    archipelago_dir = os.path.dirname(worlds_dir)
    
    sys.path.insert(0, archipelago_dir)
    sys.path.insert(0, worlds_dir)
    
    from test.bases import WorldTestBase
    from poe.poeClient import validationLogic
    
    class PoeTestBase(WorldTestBase):
        game = "Path of Exile"


class TestBossValidation(PoeTestBase):
    """Comprehensive tests for boss completion validation logic"""

    def create_mock_context(self, boss_status=None, locations=None):
        """Create a mock context with specified boss status and locations"""
        context = Mock()
        context.ctx = Mock()
        context.ctx.boss_status = boss_status or {}
        context.ctx.locations = locations or {}
        return context

    def test_check_for_victory_all_bosses_defeated(self):
        """Test victory check when all bosses are defeated"""
        boss_status = {
            "Merveil": True,
            "The Vaal Oversoul": True,
            "Dominus": True,
            "Malachai": True,
            "Innocence": True,
            "Kitava": True,
            "Elder": True,
            "Shaper": True,
            "Sirus": True
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertTrue(result, "Should return True when all bosses are defeated")

    def test_check_for_victory_no_bosses_defeated(self):
        """Test victory check when no bosses are defeated"""
        boss_status = {}
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertFalse(result, "Should return False when no bosses are defeated")

    def test_check_for_victory_partial_bosses_defeated(self):
        """Test victory check when only some bosses are defeated"""
        boss_status = {
            "Merveil": True,
            "The Vaal Oversoul": True,
            "Dominus": False,
            "Malachai": True,
            # Missing other bosses
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertFalse(result, "Should return False when not all bosses are defeated")

    def test_check_for_victory_missing_boss_entries(self):
        """Test victory check when some boss entries are missing from status"""
        boss_status = {
            "Merveil": True,
            "The Vaal Oversoul": True,
            "Dominus": True,
            # Missing Malachai, Innocence, Kitava, Elder, Shaper, Sirus
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertFalse(result, "Should return False when boss entries are missing")

    def test_check_for_victory_false_values(self):
        """Test victory check with explicitly False boss status values"""
        boss_status = {
            "Merveil": True,
            "The Vaal Oversoul": True,
            "Dominus": True,
            "Malachai": True,
            "Innocence": True,
            "Kitava": True,
            "Elder": True,
            "Shaper": True,
            "Sirus": False  # This one is not defeated
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertFalse(result, "Should return False when any boss is explicitly False")

    def test_check_for_victory_none_values(self):
        """Test victory check with None boss status values"""
        boss_status = {
            "Merveil": True,
            "The Vaal Oversoul": True,
            "Dominus": True,
            "Malachai": True,
            "Innocence": True,
            "Kitava": True,
            "Elder": True,
            "Shaper": True,
            "Sirus": None  # This should be treated as not defeated
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertFalse(result, "Should return False when any boss status is None")

    def test_check_for_victory_extra_boss_entries(self):
        """Test victory check with extra boss entries that shouldn't affect result"""
        boss_status = {
            "Merveil": True,
            "The Vaal Oversoul": True,
            "Dominus": True,
            "Malachai": True,
            "Innocence": True,
            "Kitava": True,
            "Elder": True,
            "Shaper": True,
            "Sirus": True,
            "SomeOtherBoss": False,  # Extra entry shouldn't matter
            "UnknownBoss": None     # Extra entry shouldn't matter
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertTrue(result, "Should return True when all required bosses defeated despite extra entries")

    def test_check_for_victory_case_sensitivity(self):
        """Test victory check with different case boss names"""
        boss_status = {
            "merveil": True,  # lowercase
            "THE VAAL OVERSOUL": True,  # uppercase
            "Dominus": True,
            "Malachai": True,
            "Innocence": True,
            "Kitava": True,
            "Elder": True,
            "Shaper": True,
            "Sirus": True
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertFalse(result, "Should be case sensitive for boss names")

    def test_check_for_victory_empty_context(self):
        """Test victory check with empty or None context"""
        context = Mock()
        context.ctx = None
        
        with self.assertRaises(AttributeError):
            validationLogic.check_for_victory(context)

    def test_check_for_victory_no_boss_status_attribute(self):
        """Test victory check when boss_status attribute doesn't exist"""
        context = Mock()
        context.ctx = Mock()
        # Don't set boss_status attribute
        
        with self.assertRaises(AttributeError):
            validationLogic.check_for_victory(context)

    def test_check_for_victory_individual_boss_requirements(self):
        """Test that each individual boss is required for victory"""
        required_bosses = [
            "Merveil",
            "The Vaal Oversoul", 
            "Dominus",
            "Malachai",
            "Innocence",
            "Kitava",
            "Elder",
            "Shaper",
            "Sirus"
        ]
        
        # Test missing each boss individually
        for missing_boss in required_bosses:
            with self.subTest(missing_boss=missing_boss):
                boss_status = {boss: True for boss in required_bosses if boss != missing_boss}
                context = self.create_mock_context(boss_status)
                result = validationLogic.check_for_victory(context)
                self.assertFalse(result, f"Should return False when {missing_boss} is missing")

    def test_check_for_victory_truthy_values(self):
        """Test victory check with various truthy values"""
        boss_status = {
            "Merveil": 1,  # truthy number
            "The Vaal Oversoul": "yes",  # truthy string
            "Dominus": [1],  # truthy list
            "Malachai": {"defeated": True},  # truthy dict
            "Innocence": True,
            "Kitava": True,
            "Elder": True,
            "Shaper": True,
            "Sirus": True
        }
        
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertTrue(result, "Should accept various truthy values as defeated")

    def test_check_for_victory_falsy_values(self):
        """Test victory check with various falsy values"""
        falsy_values = [False, 0, "", [], {}, None]
        
        for falsy_value in falsy_values:
            with self.subTest(falsy_value=repr(falsy_value)):
                boss_status = {
                    "Merveil": True,
                    "The Vaal Oversoul": True,
                    "Dominus": True,
                    "Malachai": True,
                    "Innocence": True,
                    "Kitava": True,
                    "Elder": True,
                    "Shaper": True,
                    "Sirus": falsy_value  # Test with falsy value
                }
                
                context = self.create_mock_context(boss_status)
                result = validationLogic.check_for_victory(context)
                self.assertFalse(result, f"Should return False for falsy value: {repr(falsy_value)}")

    def test_check_for_victory_performance(self):
        """Test victory check performance with large boss status dict"""
        # Create a large boss status dict with many extra entries
        boss_status = {}
        
        # Add required bosses
        required_bosses = [
            "Merveil", "The Vaal Oversoul", "Dominus", "Malachai",
            "Innocence", "Kitava", "Elder", "Shaper", "Sirus"
        ]
        for boss in required_bosses:
            boss_status[boss] = True
            
        # Add many extra bosses
        for i in range(1000):
            boss_status[f"ExtraBoss{i}"] = True
            
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertTrue(result, "Should handle large boss status dict efficiently")

    def test_check_for_victory_return_type(self):
        """Test that check_for_victory returns boolean type"""
        # Test True case
        boss_status = {
            "Merveil": True,
            "The Vaal Oversoul": True,
            "Dominus": True,
            "Malachai": True,
            "Innocence": True,
            "Kitava": True,
            "Elder": True,
            "Shaper": True,
            "Sirus": True
        }
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertIsInstance(result, bool, "Should return boolean type")
        self.assertTrue(result)
        
        # Test False case
        boss_status = {}
        context = self.create_mock_context(boss_status)
        result = validationLogic.check_for_victory(context)
        self.assertIsInstance(result, bool, "Should return boolean type")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
