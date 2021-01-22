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
        UpdateExpression="SET behavioral_observations_and_testing_conditions_pg1_a = :botcpg1a, behavioral_observations_and_testing_conditions_pg1_b = :botcpg1b, behavioral_observations_and_testing_conditions_pg1_c = :botcpg1c, behavioral_observations_and_testing_conditions_pg1_d = :botcpg1d, behavioral_observations_and_testing_conditions_pg1_e = :botcpg1e, behavioral_observations_and_testing_conditions_pg1_f = :botcpg1f",
        ExpressionAttributeValues={
            ":botcpg1a": event['behavioral_observations_and_testing_conditions_pg1_a'],
            ":botcpg1b": event['behavioral_observations_and_testing_conditions_pg1_b'],
            ":botcpg1c": event['behavioral_observations_and_testing_conditions_pg1_c'],
            ":botcpg1d": event['behavioral_observations_and_testing_conditions_pg1_d'],
            ":botcpg1e": event['behavioral_observations_and_testing_conditions_pg1_e'],
            ":botcpg1f": event['behavioral_observations_and_testing_conditions_pg1_f']
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
        UpdateExpression="SET behavioral_observations_and_testing_conditions_pg2_a = :botcpg2a, behavioral_observations_and_testing_conditions_pg2_b = :botcpg2b",
        ExpressionAttributeValues={
            ":botcpg2a": event['behavioral_observations_and_testing_conditions_pg2_a'],
            ":botcpg2b": event['behavioral_observations_and_testing_conditions_pg2_b']
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
        UpdateExpression="SET behavioral_observations_and_testing_conditions_pg3_a = :botcpg3a, behavioral_observations_and_testing_conditions_pg3_b = :botcpg3b, behavioral_observations_and_testing_conditions_pg3_c = :botcpg3c, behavioral_observations_and_testing_conditions_pg3_d = :botcpg3d, behavioral_observations_and_testing_conditions_pg3_e = :botcpg3e, behavioral_observations_and_testing_conditions_pg3_f = :botcpg3f, behavioral_observations_and_testing_conditions_pg3_g = :botcpg3g, behavioral_observations_and_testing_conditions_pg3_h = :botcpg3h, behavioral_observations_and_testing_conditions_pg1_i = :botcpg1i",
        ExpressionAttributeValues={
            ":botcpg3a": event['behavioral_observations_and_testing_conditions_pg3_a'],
            ":botcpg3b": event['behavioral_observations_and_testing_conditions_pg3_b'],
            ":botcpg3c": event['behavioral_observations_and_testing_conditions_pg3_c'],
            ":botcpg3d": event['behavioral_observations_and_testing_conditions_pg3_d'],
            ":botcpg3e": event['behavioral_observations_and_testing_conditions_pg3_e'],
            ":botcpg3f": event['behavioral_observations_and_testing_conditions_pg3_f'],
            ":botcpg3g": event['behavioral_observations_and_testing_conditions_pg3_g'],
            ":botcpg3h": event['behavioral_observations_and_testing_conditions_pg3_h'],
            ":botcpg3i": event['behavioral_observations_and_testing_conditions_pg3_i']
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
        UpdateExpression="SET behavioral_observations_and_testing_conditions_pg4_a = :botcpg4a, behavioral_observations_and_testing_conditions_pg4_b = :botcpg4b, behavioral_observations_and_testing_conditions_pg4_c = :botcpg4c, behavioral_observations_and_testing_conditions_pg4_d = :botcpg4d, behavioral_observations_and_testing_conditions_pg4_e = :botcpg4e, behavioral_observations_and_testing_conditions_pg4_f = :botcpg4f, behavioral_observations_and_testing_conditions_pg4_g = :botcpg4g",
        ExpressionAttributeValues={
            ":botcpg4a": event['behavioral_observations_and_testing_conditions_pg4_a'],
            ":botcpg4b": event['behavioral_observations_and_testing_conditions_pg4_b'],
            ":botcpg4c": event['behavioral_observations_and_testing_conditions_pg4_c'],
            ":botcpg4d": event['behavioral_observations_and_testing_conditions_pg4_d'],
            ":botcpg4e": event['behavioral_observations_and_testing_conditions_pg4_e'],
            ":botcpg4f": event['behavioral_observations_and_testing_conditions_pg4_f'],
            ":botcpg4g": event['behavioral_observations_and_testing_conditions_pg4_g']
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
        UpdateExpression="SET behavioral_observations_and_testing_conditions_pg5_a = :botcpg5a, behavioral_observations_and_testing_conditions_pg5_b = :botcpg5b, behavioral_observations_and_testing_conditions_pg5_c = :botcpg5c, behavioral_observations_and_testing_conditions_pg5_d = :botcpg5d, behavioral_observations_and_testing_conditions_pg5_e = :botcpg5e, behavioral_observations_and_testing_conditions_pg5_f = :botcpg5f, behavioral_observations_and_testing_conditions_pg5_g = :botcpg5g",
        ExpressionAttributeValues={
            ":botcpg5a": event['behavioral_observations_and_testing_conditions_pg5_a'],
            ":botcpg5b": event['behavioral_observations_and_testing_conditions_pg5_b'],
            ":botcpg5c": event['behavioral_observations_and_testing_conditions_pg5_c'],
            ":botcpg5d": event['behavioral_observations_and_testing_conditions_pg5_d'],
            ":botcpg5e": event['behavioral_observations_and_testing_conditions_pg5_e'],
            ":botcpg5f": event['behavioral_observations_and_testing_conditions_pg5_f'],
            ":botcpg5g": event['behavioral_observations_and_testing_conditions_pg5_g']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
