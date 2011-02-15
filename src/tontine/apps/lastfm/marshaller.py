"""Fetch data from last.fm both recent and historical.
last.fm does not provide access to your full history using
its API. We scrap your history pages instead via:

http://www.last.fm/user/username/tracks?page=2 

Otherwise we use the API methods to get fairly recent
entries.
"""

from BeautifulSoup import BeautifulSoup
from tontine.apps.utils.connections import fetch_page
from lxml import etree
from StringIO import StringIO

def get_history():
    """Scrap the web pages of the user to recover all the 
       entries."""

def _filter_page(html):
    """Take the html and return something we can work with
       using BeautifulSoup"""  
    
    print "Starting soup"
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    print tree.findall("//table/tbody/tr")  
    #print tree.xpath('//html/body/div[@id='page']/div/div[@id='content']/table[@id='deletablert']/tbody/tr[@id='r9_1546360_1408958781']/td[2]')  

def get_recent():
    """Get "recent" tracks, this uses last.fm API.
       user.gettopartists"""

    
