import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):
    PK = 'SIBLING-'+str(uuid.uuid4())
    table.put_item(
        Item={
            'PK': PK,
            'SK': event['patient_id'],
            'sibling_first_name': event['sibling_first_name'],
            'sibling_last_name': event['sibling_last_name'],
            'sibling_gender': event['sibling_gender'],
            'sibling_dob': event['sibling_dob']
        }
    )
    return response("You did it!! Sibling created successfully.", 200)


def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'message': message,
        'headers': {
            'Content-Type': 'application/json',
            'Acces-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,PUT',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
        }
    }
