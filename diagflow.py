from flask import Flask
import json
import random
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def Hello():
    return '{"Hello" : "AIDI"}'

