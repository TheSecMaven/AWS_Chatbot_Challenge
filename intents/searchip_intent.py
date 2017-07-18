import boto3
client = boto3.client('lex-models')


response = client.put_intent(
		name='xfe_findip', 
		slots=[{ 
		'name':'my_ip','description' : 'Get IP Address to Search','slotConstraint': 'Required','slotType':'IP','slotTypeVersion':'$LATEST','valueElicitationPrompt':{ 'messages':[{'contentType':'PlainText','content':'What IP?'},],'maxAttempts':3},'priority':1}]

,sampleUtterances=['ip','search ip'],
fulfillmentActivity={
        'type':'CodeHook',
        'codeHook':{
        'messageVersion':'1.0',
        'uri': 'arn:aws:lambda:us-east-1:547202050227:function:myxforce'
        },

}
)


