import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('clarityAPI')

table.put_item(
    Item={
        'Name': 'Kirk',
        'Location': 'North Pole',
        'id': str(uuid.uuid4())
    }
)
print("TABLE: ", table)
