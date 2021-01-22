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
        UpdateExpression="SET rait_pg1_a = :rpg1a, rait_pg1_b = :rpg1b",
        ExpressionAttributeValues={
            ":rpg1a": event['rait_pg1_a'],
            ":rpg1b": event['rait_pg1_b']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET rait_pg2_a = :rpg2a, rait_pg2_b = :rpg2b",
        ExpressionAttributeValues={
            ":rpg2a": event['rait_pg2_a'],
            ":rpg2b": event['rait_pg2_b']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET rait_pg3_a = :rpg3a",
        ExpressionAttributeValues={
            ":rpg3a": event['rait_pg3_a']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
