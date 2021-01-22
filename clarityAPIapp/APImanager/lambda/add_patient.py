import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):
    if (None in event.values()) or ("" in event.values()):
        return {
            'message': "Please enter values for all fields in the form."
        }
    else:
        pk = 'PATIENT-'+str(uuid.uuid4())
        table.put_item(Item={
            'PK': pk,
            'SK': event['patient_last_name'],
            'patient_first_name': event['patient_first_name'],
            'patient_middle_name': event['patient_middle_name'],
            'patient_last_name': event['patient_last_name'],
            'patient_date_of_birth': event['patient_date_of_birth'],
            'patient_referral': event['patient_referral'],
            'patient_office_time': event['patient_office_time'],
            'patient_case_number': event['patient_case_number'],
            'patient_evaluation_date': event['patient_evaluation_date'],
            'patient_county': event['patient_county'],
            'patient_interview_time': event['patient_interview_time'],
            'patient_intake_time': event['patient_intake_time'],
            'patient_gender': event['patient_gender'],

        })
        new_item = table.get_item(Key={
            'PK': pk,
            'SK': event['patient_last_name']
        })
        return {
            'statusCode': 200,
            'message': 'Patient created successfully',
            'Patient': new_item
        }
