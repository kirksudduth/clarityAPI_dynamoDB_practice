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
        UpdateExpression="SET aimsweb_plus_achievement_test_pg1_col1_a = :apatpg1c1a, aimsweb_plus_achievement_test_pg1_col1_b = :apatpg1c1b, aimsweb_plus_achievement_test_pg1_col1_c = :apatpg1c1c, aimsweb_plus_achievement_test_pg1_col1_d = :apatpg1c1d, aimsweb_plus_achievement_test_pg1_col1_e = :apatpg1c1e",
        ExpressionAttributeValues={
            ":apatpg1c1a": event['aimsweb_plus_achievement_test_pg1_col1_a'],
            ":apatpg1c1b": event['aimsweb_plus_achievement_test_pg1_col1_b'],
            ":apatpg1c1c": event['aimsweb_plus_achievement_test_pg1_col1_c'],
            ":apatpg1c1d": event['aimsweb_plus_achievement_test_pg1_col1_d'],
            ":apatpg1c1e": event['aimsweb_plus_achievement_test_pg1_col1_e']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET aimsweb_plus_achievement_test_pg1_col2_a = :apatpg1c2a, aimsweb_plus_achievement_test_pg1_col2_b = :apatpg1c2b, aimsweb_plus_achievement_test_pg1_col2_c = :apatpg1c2c, aimsweb_plus_achievement_test_pg1_col2_d = :apatpg1c2d, aimsweb_plus_achievement_test_pg1_col2_e = :apatpg1c2e",
        ExpressionAttributeValues={
            ":apatpg1c2a": event['aimsweb_plus_achievement_test_pg1_col2_a'],
            ":apatpg1c2b": event['aimsweb_plus_achievement_test_pg1_col2_b'],
            ":apatpg1c2c": event['aimsweb_plus_achievement_test_pg1_col2_c'],
            ":apatpg1c2d": event['aimsweb_plus_achievement_test_pg1_col2_d'],
            ":apatpg1c2e": event['aimsweb_plus_achievement_test_pg1_col2_e']
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
        UpdateExpression="SET aimsweb_plus_achievement_test_pg2_col1_a = :apatpg2c1a, aimsweb_plus_achievement_test_pg2_col1_b = :apatpg2c1b, aimsweb_plus_achievement_test_pg2_col1_c = :apatpg2c1c, aimsweb_plus_achievement_test_pg2_col1_d = :apatpg2c1d, aimsweb_plus_achievement_test_pg2_col1_e = :apatpg2c1e",
        ExpressionAttributeValues={
            ":apatpg2c1a": event['aimsweb_plus_achievement_test_pg2_col1_a'],
            ":apatpg2c1b": event['aimsweb_plus_achievement_test_pg2_col1_b'],
            ":apatpg2c1c": event['aimsweb_plus_achievement_test_pg2_col1_c'],
            ":apatpg2c1d": event['aimsweb_plus_achievement_test_pg2_col1_d'],
            ":apatpg2c1e": event['aimsweb_plus_achievement_test_pg2_col1_e']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET aimsweb_plus_achievement_test_pg2_col2_a = :apatpg2c2a, aimsweb_plus_achievement_test_pg2_col2_b = :apatpg2c2b, aimsweb_plus_achievement_test_pg2_col2_c = :apatpg2c2c, aimsweb_plus_achievement_test_pg2_col2_d = :apatpg2c2d, aimsweb_plus_achievement_test_pg2_col2_e = :apatpg2c2e",
        ExpressionAttributeValues={
            ":apatpg2c2a": event['aimsweb_plus_achievement_test_pg2_col2_a'],
            ":apatpg2c2b": event['aimsweb_plus_achievement_test_pg2_col2_b'],
            ":apatpg2c2c": event['aimsweb_plus_achievement_test_pg2_col2_c'],
            ":apatpg2c2d": event['aimsweb_plus_achievement_test_pg2_col2_d'],
            ":apatpg2c2e": event['aimsweb_plus_achievement_test_pg2_col2_e']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
