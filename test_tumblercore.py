# test_tumblercore.py
"""
Tests for TumblerCore module.
"""

import unittest
from tumblercore import TumblerCore

class TestTumblerCore(unittest.TestCase):
    """Test cases for TumblerCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TumblerCore()
        self.assertIsInstance(instance, TumblerCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TumblerCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
