#!/usr/bin/python3
'''blueprints for api endpoints'''
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    return {
            'status': 'OK'
            }


@app_views.route('/stats')
def stats():
    '''return count of objects in storage'''
    stats = dict()
    classes = ['City', 'Places', 'State', 'Reviews', 'Users']
    for cls in classes:
        key = cls.lower()
        stats.update({key: storage.count(cls)})
    return (stats)
