"""Main class to fire up a server and to handle url calls."""
from bottle import route, run, template
from bottle import get, post, request, debug
import os
from datetime import datetime
from pymongo import Connection

path = os.path.dirname(os.path.realpath(__file__))
template_path = path + '/templates/'

@route('/auth/:service')
def auth():
    return "Redirecting to remote service."

@route('/callback/:service')
def hello():
    return "Third party callback."

@get('/setup')
def setup_form():
    """Initial setup process."""
    return template(template_path + 'setup', title='Hello World!')

@post('/setup')
def setup_post():
    """Post from setup form"""
    lastfm_username = request.forms.get('lastfm_username')
    github = request.forms.get('github_username')
    save_lastfm_settings(lastfm_username)
    return 'success'

def save_lastfm_settings(username):
    """Save our connection details to our db."""

    connection = Connection('localhost', 27017)
    db = connection.test_database
    setting = { 'connection' : 'lastfm',
                'username' : username,
                'created' : datetime.now(),
                'request_url' : 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks'
    }

    settings = db.settings
    settings.insert(setting)

def save_github_settings(username):
    """Save our connection details to our db."""

    connection = Connection('localhost', 27017)
    db = connection.test_database
    setting = { 'connection' : 'github',
                'username' : username,
                'created' : datetime.now(),
                'request_url' : 'http://github.com'
    }

    settings = db.settings
    settings.insert(setting)

@route('/stats/:service')
def stats():
    """Generate stats for given service."""
    return "Stats"

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080)
