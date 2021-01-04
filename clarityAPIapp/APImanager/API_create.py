import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('clarityAPI')


def add_user(request):
    if request.method == 'POST':
        # put if conditional where check value of is_staff
        table.put_item(
            Item={
                'first_name': 'Tanya',
                'middle_name': 'Dayton',
                'last_name': 'Dayton',
                'email': 'email',
                'username': 'username',
                'password': 'password',
                'is_staff': True,
                'title': 'Important Person',
                'is_admin': True,
                'PK': 'EMPLOYEE#'+str(uuid.uuid4()),
                'SK': 'LOCATION#2'
            }
        )


def add_patient(request):
    if request.method == 'POST':
        table.put_item(
            Item={
                'first_name': {form_value.first_name},
                'middle_name': {form_value.middle_name},
                'last_name': {form_value.last_name},
                'dob': {form_value.dob},
                'referral': {form_value.referral},
                'office_time': {form_value.office_time},
                'report_writing': {form_value.report_writing},
                'case_no': {form_value.case_no},
                'evaluation_date': {form_value.evaluation_date},
                'county': {form_value.county},
                'interview_time': {form_value.interview_time},
                'intake_time': {form_value.intake_time},
                'PK': 'PATIENT#'+str(uuid.uuid4()),
                'SK': {form_value.county}
            }
        )
