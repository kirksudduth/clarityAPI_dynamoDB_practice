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
        UpdateExpression="SET parenting_pg1_a = :ppg1a, parenting_pg1_b = :ppg1b, parenting_pg1_c = :ppg1c",
        ExpressionAttributeValues={
            ":ppg1a": event['parenting_pg1_a'],
            ":ppg1b": event['parenting_pg1_b'],
            ":ppg1c": event['parenting_pg1_c']
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
        UpdateExpression="SET parenting_pg2_a = :ppg2a, parenting_pg2_b = :ppg2b, parenting_pg2_c = :ppg2c",
        ExpressionAttributeValues={
            ":ppg2a": event['parenting_pg2_a'],
            ":ppg2b": event['parenting_pg2_b'],
            ":ppg2c": event['parenting_pg2_c']
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
        UpdateExpression="SET parenting_pg3_a = :ppg3a, parenting_pg3_b = :ppg3b",
        ExpressionAttributeValues={
            ":ppg3a": event['parenting_pg3_a'],
            ":ppg3b": event['parenting_pg3_b']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
