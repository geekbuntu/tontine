"""Fetch data from last.fm both recent and historical.
last.fm does not provide access to your full history using
its API. We scrap your history pages instead via:

http://www.last.fm/user/username/tracks?page=2 

Otherwise we use the API methods to get fairly recent
entries.
"""

from tontine.apps.utils.connections import fetch_page

def get_history():
    """Scrap the web pages of the user to recover all the 
       entries."""
    # use getrecentttracks and page through it

def _filter_page(html):
    """Take the html and return something we can work with
       using BeautifulSoup"""  
    
    pass
def get_recent():
    """Get "recent" tracks, this uses last.fm API.
       user.gettopartists"""
