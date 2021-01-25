import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):
    pk = 'SPOUSE-'+str(uuid.uuid4())
    response = table.put_item(
        Item={
            'PK': pk,
            'SK': event['patient_id'],
            'spouse_first_name': event['spouse_first_name'],
            'spouse_last_name': event['spouse_last_name'],
            'spouse_gender': event['spouse_gender'],
            'spouse_dob': event['spouse_dob']
        }
    )

    item = table.get_item(Key={"PK": pk, "SK": event['patient_id']})

    return response("Spouse added successfully!", 200)


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
