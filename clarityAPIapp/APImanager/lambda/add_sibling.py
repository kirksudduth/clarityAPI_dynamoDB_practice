import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):

    response = table.put_item(
        Item={
            'PK': 'SIBLING-'+str(uuid.uuid4()),
            'SK': event['patient_id'],
            'sibling_first_name': event['sibling_first_name'],
            'sibling_last_name': event['sibling_last_name'],
            'sibling_gender': event['sibling_gender'],
            'sibling_dob': event['sibling_dob']
        }
    )
    return response
