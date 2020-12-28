import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('clarityAPI')

table.put_item(
    Item={
        'First_Name': 'Jack',
        'Location': 'North Pole',
        'id': str(uuid.uuid4())
    }
)
print("TABLE: ", table)
