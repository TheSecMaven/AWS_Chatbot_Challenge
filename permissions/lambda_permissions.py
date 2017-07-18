import boto3
client = boto3.client('lambda')

response = client.add_permission(
    Action='lambda:*',
    FunctionName='myxforce',
    Principal='lex.amazonaws.com',
    StatementId='ID-1',
)

