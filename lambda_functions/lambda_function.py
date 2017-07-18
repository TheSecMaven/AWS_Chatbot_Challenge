#Sayhi function.Establishes the xforce key and password in the session so that other intents can work without prompting for passcodes again

from __future__ import print_function

import json

print('Loading function')

def lambda_handler(event, context):
    name = event['currentIntent']['slots']['name']
    key = event['currentIntent']['slots']['xforcekey']
    password = event['currentIntent']['slots']['xforcepassword']

    toreturn = { "sessionAttributes": {
    "name": str(name),'xforcekey': str(key),'xforcepassword': str(password),
  },"dialogAction": {"type": "Close","fulfillmentState": "Fulfilled","message": {"contentType": "PlainText","content": "Message to convey to " + str(name) + ". For example, Thanks, your pizza has been ordered."}}}
    return (toreturn) 
