"""Methods for fetching and carrying from remote connections."""

import httplib2

def fetch_page(url):
    """Return the raw html of the page requested."""

    h = httplib2.Http()
    resp, content = h.request(url, "GET")
    
    # return if we are successful
    if resp['status'] == 200:
        return content
