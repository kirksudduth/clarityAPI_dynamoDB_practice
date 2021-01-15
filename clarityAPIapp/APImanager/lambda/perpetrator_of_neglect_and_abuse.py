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
        UpdateExpression="SET perpetrator_of_neglect_and_abuse_pg1_a = :pnapg1a, perpetrator_of_neglect_and_abuse_pg1_b = :pnapg1b, perpetrator_of_neglect_and_abuse_pg1_c = :pnapg1c",
        ExpressionAttributeValues={
            ":pnapg1a": event['perpetrator_of_neglect_and_abuse_pg1_a'],
            ":pnapg1b": event['perpetrator_of_neglect_and_abuse_pg1_b'],
            ":pnapg1c": event['perpetrator_of_neglect_and_abuse_pg1_c']
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
        UpdateExpression="SET perpetrator_of_neglect_and_abuse_pg2_a = :pnapg2a, perpetrator_of_neglect_and_abuse_pg2_b = :pnapg2b, perpetrator_of_neglect_and_abuse_pg2_c = :pnapg2c",
        ExpressionAttributeValues={
            ":pnapg2a": event['perpetrator_of_neglect_and_abuse_pg2_a'],
            ":pnapg2b": event['perpetrator_of_neglect_and_abuse_pg2_b'],
            ":pnapg2c": event['perpetrator_of_neglect_and_abuse_pg2_c']
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
        UpdateExpression="SET perpetrator_of_neglect_and_abuse_pg3_a = :pnapg3a, perpetrator_of_neglect_and_abuse_pg3_b = :pnapg3b, perpetrator_of_neglect_and_abuse_pg3_c = :pnapg3c",
        ExpressionAttributeValues={
            ":pnapg3a": event['perpetrator_of_neglect_and_abuse_pg3_a'],
            ":pnapg3b": event['perpetrator_of_neglect_and_abuse_pg3_b'],
            ":pnapg3c": event['perpetrator_of_neglect_and_abuse_pg3_c']
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
        UpdateExpression="SET perpetrator_of_neglect_and_abuse_pg4_a = :pnapg4a",
        ExpressionAttributeValues={
            ":pnapg4a": event['perpetrator_of_neglect_and_abuse_pg4_a']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
