from flask import Flask, send_from_directory
from tweepywrapper import TweepyWrapper
import json
app = Flask(__name__)



### This should eventually get replaced with a redirect/ & static content served through NGNIX/APACHE2
@app.route('/')
def index():
    return send_from_directory('static','index.html')

@app.route('/us.json')
def usJson():
    return send_from_directory('static','us.json')

@app.route('/twitter/search/')
def twitterSearch():
	tweepywrapper = TweepyWrapper()
	return json.dumps(tweepywrapper.search("#trump"))