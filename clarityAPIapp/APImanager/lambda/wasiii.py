import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wasiii_pg1_col1_a = :wasiiipg1c1a, wasiii_pg1_col1_b = :wasiiipg1c1b, wasiii_pg1_col1_c = :wasiiipg1c1c, wasiii_pg1_col1_d = :wasiiipg1c1d",
        ExpressionAttributeValues={
            ":wasiiipg1c1a": event['wasiii_pg1_col1_a'],
            ":wasiiipg1c1b": event['wasiii_pg1_col1_b'],
            ":wasiiipg1c1c": event['wasiii_pg1_col1_c'],
            ":wasiiipg1c1d": event['wasiii_pg1_col1_d']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wasiii_pg1_col2_a = :wasiiipg1c2a, wasiii_pg1_col2_b = :wasiiipg1c2b, wasiii_pg1_col2_c = :wasiiipg1c2c, wasiii_pg1_col2_d = :wasiiipg1c2d",
        ExpressionAttributeValues={
            ":wasiiipg1c2a": event['wasiii_pg1_col2_a'],
            ":wasiiipg1c2b": event['wasiii_pg1_col2_b'],
            ":wasiiipg1c2c": event['wasiii_pg1_col2_c'],
            ":wasiiipg1c2d": event['wasiii_pg1_col2_d']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
