"""Test the access methods for the last.fm app"""

import unittest, os
from tontine.apps.lastfm.marshaller import _filter_page

class TestLastfmKey(unittest.TestCase):
    """Test that we can access the service and process correctly."""

    def setUp(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
    
    def tearDown(self):
        pass

    def test_filter_page(self):
        """Test we get the expected results from converting
            a history page from html to something."""

        html_file = open(self.path + '/test_data/raw_history_page.html', 'r')
        html = html_file.read()
        html_file.close()

        _filter_page(html)

if __name__ == '__main__':
    unittest.main()

