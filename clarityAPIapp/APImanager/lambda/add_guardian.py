import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):
    pk = 'GUARDIAN-'+str(uuid.uuid4())
    response = table.put_item(
        Item={
            'PK': pk,
            'SK': event['patient_id'],
            'patient_guardian_first_name': event['patient_guardian_first_name'],
            'patient_guardian_last_name': event['patient_guardian_last_name'],
            'patient_guardian_gender': event['patient_guardian_gender']
        }
    )

    item = table.get_item(Key={"PK": pk, "SK": event['patient_id']})

    return {
        'statusCode': 200,
        'message': json.dumps("Beeeeautiful!"),
        'NewGuardianItem': item['Item']
    }
