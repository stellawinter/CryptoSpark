# test_cryptospark.py
"""
Tests for CryptoSpark module.
"""

import unittest
from cryptospark import CryptoSpark

class TestCryptoSpark(unittest.TestCase):
    """Test cases for CryptoSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoSpark()
        self.assertIsInstance(instance, CryptoSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
