from flask import Flask, request
import json
import random
import requests

app = Flask(__name__)
app.debug = True

# @app.route('/')
# def Hello():
#     return '{"Hello" : "World"}'

# @app.route('/webhook',methods=['POST'])
@app.route('/')
def index():
    #Get the formula1-gossip entity from the dialogflow fullfilment request.
    # body = request.json
    # series = body['queryResult']['parameters']['series-checker']
    # season = body['queryResult']['parameters']['season-checker']
    # round = body['queryResult']['parameters']['round-checker']

    #Connect to the API anf get the JSON file.
    # api_url = 'http://ergast.com/api/'+series+'/'+season+'/'+round+'/results.json'
    api_url = 'http://ergast.com/api/f1/2021/1/results.json'
    headers = {'Content-Type': 'application/json'} #Set the HTTP header for the API request
    response = requests.get(api_url, headers=headers) #Connect to f1 API and read the JSON response.
    r=response.json() #Convert the JSON string to a dict for easier parsing.

    #Extract weather data we want from the dict and conver to strings to make it easy to generate the dialogflow reply.
    given_name = str(r["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["givenName"])
    family_name = str(r["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["familyName"])

    #Build the Dialogflow reply.
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The winner was ' + given_name + ' ' + family_name + '"] } } ]}'
    return reply   