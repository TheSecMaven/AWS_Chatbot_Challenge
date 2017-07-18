import boto3
client = boto3.client('lex-models')

response = client.put_bot(
    name="Information_Security",
    description="A conversational bot for pulling threat intelligence information from Third Party APIs ",
    intents=[{ 
        'intentName':'xforce',
        'intentVersion':"$LATEST"
        },
	{'intentName':'xfe_findip',
	'intentVersion':'$LATEST'}
   ],
clarificationPrompt = {
    'messages':[
               { 
                   'contentType': 'PlainText',
                   'content':"Sorry. I can't seem to understand you"
               },
       ],
    'maxAttempts':3,
    'responseCard': 'THis is my first response card'
   },
abortStatement={
  'messages':[{
    'contentType': 'PlainText',
    'content': "You have a weird voice so I'm aborting this operation" },],
    'responseCard':'We aborted this stuff because it got too hard' },
idleSessionTTLInSeconds=200,
voiceId='Joey',
processBehavior='SAVE',
locale='en-US',
childDirected=False
)
