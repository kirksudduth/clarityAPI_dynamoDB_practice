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
        print("TABLE: ", table)
