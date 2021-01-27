import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):

    response = table.query(
        KeyConditionExpression=Key('PK').eq(
            'PATIENT') & Key('SK').begins_with('PATIENT')
    )

    return response['Items']
