import json
import boto3
import os

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['CHARACTER_TABLE'])

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    response = table.scan(Select='ALL_ATTRIBUTES')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': json.dumps(response['Items'])
    }
