import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):
    pk = 'CHILD-'+str(uuid.uuid4())
    response = table.put_item(
        Item={
            'PK': pk,
            'SK': event['patient_id'],
            'child_first_name': event['child_first_name'],
            'child_last_name': event['child_last_name'],
            'child_gender': event['child_gender'],
            'child_dob': event['child_dob']
        }
    )

    item = table.get_item(Key={"PK": pk, "SK": event['patient_id']})

    return {
        'statusCode': 200,
        'message': json.dumps("Beeeeautiful!"),
        'NewChildItem': item['Item']
    }
