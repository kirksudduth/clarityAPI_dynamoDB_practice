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
        UpdateExpression="SET substance_abuse_subtle_screening_inventory_4_a = :sassi4a, substance_abuse_subtle_screening_inventory_4_b = :sassi4b, substance_abuse_subtle_screening_inventory_4_c = :sassi4c, substance_abuse_subtle_screening_inventory_4_d = :sassi4d",
        ExpressionAttributeValues={
            ":sassi4a": event['substance_abuse_subtle_screening_inventory_4_a'],
            ":sassi4b": event['substance_abuse_subtle_screening_inventory_4_b'],
            ":sassi4c": event['substance_abuse_subtle_screening_inventory_4_c'],
            ":sassi4d": event['substance_abuse_subtle_screening_inventory_4_d']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
