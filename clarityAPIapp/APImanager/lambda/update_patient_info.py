import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET patient_referral = :pr, patient_office_time = :pot, patient_case_number = :pcn, patient_evaluation_date = :ped, patient_county = :pc, patient_interview_time = :pit, patient_intake_time = :pint",
        ExpressionAttributeValues={
            ":pr": event['patient_referral'],
            ":pot": event['patient_office_time'],
            ":pcn": event['patient_case_number'],
            ":ped": event['patient_evaluation_date'],
            ":pc": event['patient_county'],
            ":pit": event['patient_interview_time'],
            ":pint": event['patient_intake_time']
        },
        ReturnValues="UPDATED_NEW")
    return response("It worked!", 200)


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
