import requests
import sys
import json
from optparse import OptionParser
import hashlib
import mybase64


global IP_Location
IP_Location = ""
def send_request(apiurl, scanurl, headers):
    fullurl = apiurl +  scanurl
    response = requests.get(fullurl, params='', headers=headers, timeout=20)
    all_json = response.json()
    return all_json

def get_current_info(column_number,review_count,Provided_IP,all_json):    #This function pulls current information from JSON output for a handful of keys
    keys = ["categoryDescriptions","created","score"]
    attr = keys[column_number]
    key_count = 0
    current_info = ""
    if attr == "created" or attr == "score":         #If the attribute we are looking for is the created date or score
        return all_json["history"][review_count-1][attr]
    else:
        for key in all_json["history"][review_count-1][attr]:
            if (key_count >= 1):
                current_info = current_info + " ," + str(key)
            else:
                current_info = str(key)
                key_count += 1
        return current_info

def get_md5(filename):
    try:
        f = open(filename,"rb")
        md5 = hashlib.md5((f).read()).hexdigest()
        return md5
    except e:
        print str(e)
def startfunc(IP,key,password):
    key = key
    password = password

    token = mybase64.b64encode(key + ":" + password)
    print token
    headers = {'Authorization': "Basic " + token, 'Accept': 'application/json'}
    url = "https://api.xforce.ibmcloud.com:443"
    scanurl = IP
    apiurl = url + "/ipr/"
    all_json = send_request(apiurl, scanurl, headers)
    apiurl = url + "/ipr/malware/"
    send_request(apiurl, scanurl, headers)
    apiurl = url + "/ipr/history/"
    historic = send_request(apiurl, scanurl, headers)
    print(historic)
    already_categorized=[]                      #Declarations
    key_count = 0
    category_count = 0
    review_count = len(historic['history'])
    all_categories = ""

    for key in historic['history']:            #For every entry in the json output 
        for entry in key["categoryDescriptions"]:      #For every categorization within that entrys "categoryDescriptions
            if(entry in already_categorized):               #If this categorization has already been reported, don't report it again
                continue
            else:       #Since we already have this IP in our DB,
            
            
                if category_count == 0:
                    all_categories = str(entry)
                    category_count += 1
                else:
                    all_categories = all_categories + " , " + str(entry)
                    category_count += 1 


                already_categorized.append(entry)   #Add the category to the list of already printed categories so we don't repeat

    toreturn = {'categories': all_categories,'geolocation':all_json["geo"]["country"],'score': str(get_current_info(2,review_count,scanurl,all_json))}
    return toreturn

#print all_json['history'][0]['created']

#print all_json['history'][3]['categoryDescriptions']['Malware']


def lambda_handler(event, context):
    IP = event['currentIntent']['slots']['my_ip']
    name = event['sessionAttributes']['name']
    key = event['sessionAttributes']['xforcekey']
    password = event['sessionAttributes']['xforcepassword']
    print IP
    print key
    print password
    information = startfunc(IP,key,password)
    print information
    IP_Location = information['geolocation']
    IP_Category = information['categories']
    IP_Score = information['score']
    toreturn = { "sessionAttributes": {
    "name": str(name),'xforcekey': str(key),'xforcepassword': str(password)},"dialogAction": {"type": "Close","fulfillmentState": "Fulfilled","message": {"contentType": "PlainText","content":"IP: "+ str(IP) + "\n\nGeolocation is " + IP_Location + "\n\nCurrent Categorizations: " + IP_Category + "\n\nCurrent Score: " + IP_Score}}}
    return (toreturn) 