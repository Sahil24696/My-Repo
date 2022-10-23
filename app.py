from flask import Flask, request
import json
import random
import requests

app = Flask(__name__)
app.debug = True

# ROUTE 1 - to print my student number in JSON format
@app.route('/')
def studentNumber():
    dictionary =  {"Student Number" : "200506536"}
    return json.dumps(dictionary)

# ROUTE 2 - code to run the diagflow fullfilment
@app.route('/webhook',methods=['POST'])
def index():
    #Get the formula1-gossip entity from the dialogflow fullfilment request.
    body = request.json
    series = body['queryResult']['parameters']['series-checker']
    season = body['queryResult']['parameters']['season-checker']
    round = body['queryResult']['parameters']['round-checker']

    #Connect to the API and get the JSON file.
    api_url = 'http://ergast.com/api/'+series+'/'+season+'/'+round+'/results.json'
    #Set the HTTP header for the API request
    headers = {'Content-Type': 'application/json'} 
    #Connect to f1 API and read the JSON response.
    response = requests.get(api_url, headers=headers) 
    #Convert the JSON string to a dict for easier parsing.
    r=response.json()

    #Extract first & last name from the dict and conver to strings to make it easy to generate the dialogflow reply.
    given_name = str(r["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["givenName"])
    family_name = str(r["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["familyName"])

    #Build the Dialogflow reply.
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The winner was ' + given_name + ' ' + family_name + '"] } } ]}'
    return reply   
