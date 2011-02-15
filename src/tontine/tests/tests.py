import unittest
from tontine.hellfish import save_lastfm_settings
from pymongo import Connection

class TestHellfish(unittest.TestCase):
    """Test the main handler for tontine"""

    def setUp(self):
        print "starting!"
        self.connection = Connection()

    def tearDown(self):
        pass

    def test_lastfm_settings((self):
        """Test saving a last.fm setting."""
        save_lastfm_settings('bassdread')
        db = connection.test_database
        print settings.find_one()
        #self.assertEquals(setup_post(),'bassdread')


if __name__ == '__main__':
    unittest.main()
