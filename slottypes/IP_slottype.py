import boto3
client = boto3.client('lex-models')

response = client.put_slot_type(
    name='IP',
    description='Accept IP Addresses as Input',
    enumerationValues=[
        {
            'value': '123.132.169.198',
            'value':'43.223.22.123',
            'value':'1.2.3.4',
            'value':'144.32.96.55'
        }
    ],
)
