import json


def send_email(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'MessageId': 'ock-message-id'})
    }