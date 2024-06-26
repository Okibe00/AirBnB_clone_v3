#!/usr/bin/python3
'''This a minimal api module for the airbnb clone'''

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def clean_up(e):
    '''close storage session'''
    storage.close()


@app.errorhandler(404)
def error_404(e):
    '''handle 404 error'''
    return {'error': 'Not found'}, 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True, debug=True)
