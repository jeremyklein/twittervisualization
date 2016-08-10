from flask import Flask, send_from_directory
app = Flask(__name__)



### This should eventually get replaced with a redirect/ & static content served through NGNIX/APACHE2
@app.route('/')
def index():
    return send_from_directory('static','index.html')
