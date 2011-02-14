"""Main class to fire up a server and to handle url calls."""
from bottle import route, run, template
import os 

path = os.path.dirname(os.path.realpath(__file__))
template_path = path + '/templates/'

@route('/auth/:service')
def auth():
    return "Redirecting to remote service."

@route('/callback/:service')
def hello():
    return "Third party callback."

@route('/setup')
def setup():
    """Initial setup process."""
    return template(template_path + 'setup', title='Hello World!')

@route('/stats/:service')
def stats():
    """Generate stats for given service."""
    return "Stats"

run(host='localhost', port=8080)
