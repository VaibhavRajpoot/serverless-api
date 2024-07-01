import json
import boto3
import logging
from botocore.exceptions import ClientError


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def send_email(event, context):
    logger.info('Received event: %s', event)

    try:
        
        body = json.loads(event['body'])
        logger.info('Parsed body: %s', body)
        
        receiver_email = body['receiver_email']
        subject = body['subject']
        body_text = body['body_text']
        
        
        client = boto3.client('ses', region_name='us-east-1')

        
        response = client.send_email(
            Source='vaibhavrajpoot49@gmail.com', 
            Destination={
                'ToAddresses': [receiver_email],
            },
            Message={
                'Subject': {
                    'Data': subject,
                },
                'Body': {
                    'Text': {
                        'Data': body_text,
                    },
                },
            },
        )

        logger.info('Email sent response: %s', response)

       
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully", "response": response})
        }

    except ClientError as e:
        logger.error('ClientError: %s', e)
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    except Exception as e:
        logger.error('Exception: %s', e)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error", "message": str(e)})
        }
