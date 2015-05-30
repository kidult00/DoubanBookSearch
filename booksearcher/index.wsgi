# -*- coding: utf-8 -*-

import os 
import sys
import json 

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

import sae
from bottle import Bottle, request, run, template
from baymax import robot 

app = Bottle()

@app.route('/')
def hello():
    return "Hello, world! - Bottle"

# wechat request forward to robot
app.mount('/api', robot.wsgi)

application = sae.create_wsgi_app(app)