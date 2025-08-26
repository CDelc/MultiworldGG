"""
Path of Exile test module for Archipelago
"""
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
    from test.bases import WorldTestBase
    
    class PoeTestBase(WorldTestBase):
        game = "Path of Exile"
        
except ImportError:
    # Fallback for when running tests outside of normal Archipelago structure
    import unittest
    
    class PoeTestBase(unittest.TestCase):
        game = "Path of Exile"
        
        def setUp(self):
            super().setUp()


