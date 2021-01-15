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
        UpdateExpression="SET partner_relationship_pg1_a = :prpg1a, partner_relationship_pg1_b = :prpg1b, partner_relationship_pg1_c = :prpg1c, partner_relationship_pg1_d = :prpg1d, partner_relationship_pg1_e = :prpg1e",
        ExpressionAttributeValues={
            ":prpg1a": event['partner_relationship_pg1_a'],
            ":prpg1b": event['partner_relationship_pg1_b'],
            ":prpg1c": event['partner_relationship_pg1_c'],
            ":prpg1d": event['partner_relationship_pg1_d'],
            ":prpg1e": event['partner_relationship_pg1_e']
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
        UpdateExpression="SET partner_relationship_pg2_a = :prpg2a, partner_relationship_pg2_b = :prpg2b, partner_relationship_pg2_c = :prpg2c",
        ExpressionAttributeValues={
            ":prpg2a": event['partner_relationship_pg2_a'],
            ":prpg2b": event['partner_relationship_pg2_b'],
            ":prpg2c": event['partner_relationship_pg2_c']
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
        UpdateExpression="SET partner_relationship_pg3_a = :prpg3a, partner_relationship_pg3_b = :prpg3b, partner_relationship_pg3_c = :prpg3c",
        ExpressionAttributeValues={
            ":prpg3a": event['partner_relationship_pg3_a'],
            ":prpg3b": event['partner_relationship_pg3_b'],
            ":prpg3c": event['partner_relationship_pg3_c']
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
        UpdateExpression="SET partner_relationship_pg4_a = :prpg4a, partner_relationship_pg4_b = :prpg4b, partner_relationship_pg4_c = :prpg4c",
        ExpressionAttributeValues={
            ":prpg4a": event['partner_relationship_pg4_a'],
            ":prpg4b": event['partner_relationship_pg4_b'],
            ":prpg4c": event['partner_relationship_pg4_c']
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
        UpdateExpression="SET partner_relationship_pg5_a = :prpg5a, partner_relationship_pg5_b = :prpg5b, partner_relationship_pg5_c = :prpg5c",
        ExpressionAttributeValues={
            ":prpg5a": event['partner_relationship_pg5_a'],
            ":prpg5b": event['partner_relationship_pg5_b'],
            ":prpg5c": event['partner_relationship_pg5_c']
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
        UpdateExpression="SET partner_relationship_pg6_a = :prpg6a, partner_relationship_pg6_b = :prpg6b, partner_relationship_pg6_c = :prpg6c",
        ExpressionAttributeValues={
            ":prpg6a": event['partner_relationship_pg6_a'],
            ":prpg6b": event['partner_relationship_pg6_b'],
            ":prpg6c": event['partner_relationship_pg6_c']
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
        UpdateExpression="SET partner_relationship_pg7_a = :prpg7a, partner_relationship_pg7_b = :prpg7b, partner_relationship_pg7_c = :prpg7c",
        ExpressionAttributeValues={
            ":prpg7a": event['partner_relationship_pg7_a'],
            ":prpg7b": event['partner_relationship_pg7_b'],
            ":prpg7c": event['partner_relationship_pg7_c']
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
        UpdateExpression="SET partner_relationship_pg8_a = :prpg8a, partner_relationship_pg8_b = :prpg8b, partner_relationship_pg8_c = :prpg8c",
        ExpressionAttributeValues={
            ":prpg8a": event['partner_relationship_pg8_a'],
            ":prpg8b": event['partner_relationship_pg8_b'],
            ":prpg8c": event['partner_relationship_pg8_c']
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
        UpdateExpression="SET partner_relationship_pg9_a = :prpg9a, partner_relationship_pg9_b = :prpg9b, partner_relationship_pg9_c = :prpg9c",
        ExpressionAttributeValues={
            ":prpg9a": event['partner_relationship_pg9_a'],
            ":prpg9b": event['partner_relationship_pg9_b'],
            ":prpg9c": event['partner_relationship_pg9_c']
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
        UpdateExpression="SET partner_relationship_pg10_a = :prpg10a",
        ExpressionAttributeValues={
            ":prpg10a": event['partner_relationship_pg10_a']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
