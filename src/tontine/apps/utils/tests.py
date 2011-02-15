"""Test util functions"""

import unittest
from tontine.apps.utils import database

class TestDatabase(unittest.TestCase):
    """Test our database helper class"""

    def setUp(self):
        self.db_helper = DatabseHelper()
    
    def tearDown(self):
        pass

    def test_connect_database(self):
        """Test we can connect to the database"""
        
        self.db_helper()
