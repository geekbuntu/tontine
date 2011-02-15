import unittest
from tontine.hellfish import save_lastfm_settings, save_github_settings
from pymongo  import Connection
import time

class TestHellfish(unittest.TestCase):
    """Test the main handler for tontine"""

    def setUp(self):
        self.connection = Connection()
        self.username = 'username'

    def test_lastfm_settings(self):
        """Test saving a last.fm setting."""

        save_lastfm_settings(self.username)
        time.sleep(1)
        db = self.connection.test_database

        settings = db.settings
        setting = settings.find_one({'username' : 'username'})
        self.assertEquals(setting['username'], self.username)
        
        setting = settings.find_one({'connection' : 'lastfm'})
        setting = settings.find_one({'connection' : 'lastfm'})
        self.assertEquals(setting['connection'], 'lastfm')

    def test_github_settings(self):
        """Test saving a github.com setting."""

        save_github_settings(self.username)
        time.sleep(1)
        db = self.connection.test_database
        settings = db.settings  
        setting = settings.find_one({'connection' : 'github'})
        self.assertEquals(setting['username'], self.username)

        setting = settings.find_one({'connection' : 'github'})
        self.assertEquals(setting['connection'], 'github')

    def tearDown(self):
        """Clean up after ourselves"""
        
        db = self.connection.test_database
        settings = db.settings
        settings.remove({'username' : self.username})
    
        # check they are all deleted
        settings = db.settings
        self.assertEqual(settings.find_one(), None)


if __name__ == '__main__':
    unittest.main()
