"""Helper class to provice a layer between apps and the database"""
import pymongo

class DatabaseHelper(object):
    """Provice access to database"""

    def __init__(self):
        """Setup a db connection"""

        self.connection = Connection('localhost', 27017)
