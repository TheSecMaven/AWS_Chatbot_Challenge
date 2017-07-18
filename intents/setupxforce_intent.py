import boto3
client = boto3.client('lambda')
response = client.list_versions_by_function(
    FunctionName='myxforce',
    MaxItems=123
)
print (response)
client = boto3.client('lex-models')


response = client.put_intent(
		name='xforce', 
		slots=[{ 
		'name':'name','description' : 'Get User Name','slotConstraint': 'Required','slotType':'AMAZON.US_FIRST_NAME','valueElicitationPrompt':{ 'messages':[{'contentType':'PlainText','content':'What is your Name?'},],'maxAttempts':3},'priority':1},

{ 
		'name':'xforcekey','description' : 'Get xforce API key','slotConstraint': 'Required','slotType':'xforcekeys','slotTypeVersion':'$LATEST','valueElicitationPrompt':{ 'messages':[{'contentType':'PlainText','content':'What is your XForce API Key?'},],'maxAttempts':3},'priority':2}, 
{
		'name':'xforcepassword','description' : 'Get xforce API Password','slotConstraint': 'Required','slotType':'xforcekeys','slotTypeVersion':'$LATEST','valueElicitationPrompt':{ 'messages':[{'contentType':'PlainText','content':'What is your XForce API Password?'},],'maxAttempts':3},'priority':3}]

,sampleUtterances=['setup xforce'],
fulfillmentActivity={
        'type':'CodeHook',
        'codeHook':{
        'messageVersion':'1.0',
        'uri': 'arn:aws:lambda:us-east-1:547202050227:function:sayhi'
        },

}
)


