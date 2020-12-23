from pprint import pprint
import boto3


def update(id)


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('clarityAPI')

response = table.update_item(
    Key={
        'id': '2e766be3-df3c-48e0-8754-bf415e059a02'
    },
    UpdateExpression="set "
)
