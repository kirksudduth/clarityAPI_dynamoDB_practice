import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):
    PK = 'CHILD-'+str(uuid.uuid4())
    response = table.put_item(
        Item={
            'PK': PK,
            'SK': event['patient_id'],
            'child_first_name': event['child_first_name'],
            'child_last_name': event['child_last_name'],
            'child_gender': event['child_gender'],
            'child_dob': event['child_dob']
        }
    )

    item = table.get_item(Key={"PK": pk, "SK": event['patient_id']})

    return response("Child created successfully!", 200)


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
