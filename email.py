import boto3
from botocore.exceptions import ClientError

ses = boto3.client('ses')

def send_email(event, context):
    try:
        receiver_email = event['receiver_email']
        subject = event['subject']
        body_text = event['body_text']

        response = ses.send_email(
            Source='vaibhavrajpoot46@gmail.com',
            Destination={
                'ToAddresses': [receiver_email],
                'CcAddresses': [],
                'BccAddresses': []
            },
            Message={
                'Body': {
                    'Text': {
                        'Data': body_text
                    }
                },
                'Subject': {
                    'Data': subject
                }
            }
        )

        return {
            'statusCode': 200,
            'body': 'Email sent successfully!'
        }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error sending email: ' + str(e)
        }

    except KeyError as e:
        return {
            'statusCode': 400,
            'body': 'Missing required parameter: ' + str(e)
        }

