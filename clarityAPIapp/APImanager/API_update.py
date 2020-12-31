from pprint import pprint
import boto3


def update_person(pk, sk, person_name):

    dynamodb = boto3.resource(
        'dynamodb')

    table = dynamodb.Table('clarityAPI')

    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        UpdateExpression="set First_Name=:f",
        ExpressionAttributeValues={
            ':f': person_name
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


update_person('EMPLOYEE#f3235b7a-4e72-4101-afd8-6e1812c04761',
              'LOCATION#2', 'Terry')
