import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('clarityAPI')

table.put_item(
    Item={
        'First_Name': 'Tanya',
        'Location': 'Dayton',
        'PK': 'EMPLOYEE#'+str(uuid.uuid4()),
        'SK': 'LOCATION#2'
    }
)
print("TABLE: ", table)
