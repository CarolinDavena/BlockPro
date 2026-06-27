# test_blockpro.py
"""
Tests for BlockPro module.
"""

import unittest
from blockpro import BlockPro

class TestBlockPro(unittest.TestCase):
    """Test cases for BlockPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockPro()
        self.assertIsInstance(instance, BlockPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
