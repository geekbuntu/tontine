import unittest
from tontine.hellfish import save_lastfm_settings, save_github_settings
from pymongo  import Connection
import time

class TestHellfish(unittest.TestCase):
    """Test the main handler for tontine"""

    def setUp(self):
        pass
    
    def tearDown(self):
        """Clean up after ourselves"""
        pass

if __name__ == '__main__':
    unittest.main()
