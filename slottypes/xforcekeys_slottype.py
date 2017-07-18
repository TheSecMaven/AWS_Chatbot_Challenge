import boto3
client = boto3.client('lex-models')

response = client.put_slot_type(
    name='xforcekeys',
    description='Accept XForce API Keys/Passwords as input',
    enumerationValues=[
        {
            'value': '90B89072-7f3m-453m-8rel-63r3aerlca564'
        },
    ],
)
