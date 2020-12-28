from pprint import pprint
import boto3


def update_person(id, person_name):

    dynamodb = boto3.resource(
        'dynamodb')

    table = dynamodb.Table('clarityAPI')

    response = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression="set First_Name=:f",
        ExpressionAttributeValues={
            ':f': person_name
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


update_person('65146075-eaf6-4f89-939d-3fc2a44aa339', 'John')
