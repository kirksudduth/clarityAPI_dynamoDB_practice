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
        UpdateExpression="SET wide_range_achievement_test_5_pg1_col1_a = :wrat5pg1c1a, wide_range_achievement_test_5_pg1_col1_b = :wrat5pg1c1b, wide_range_achievement_test_5_pg1_col1_c = :wrat5pg1c1c, wide_range_achievement_test_5_pg1_col1_d = :wrat5pg1c1d, wide_range_achievement_test_5_pg1_col1_e = :wrat5pg1c1e",
        ExpressionAttributeValues={
            ":wrat5pg1c1a": event['wide_range_achievement_test_5_pg1_col1_a'],
            ":wrat5pg1c1b": event['wide_range_achievement_test_5_pg1_col1_b'],
            ":wrat5pg1c1c": event['wide_range_achievement_test_5_pg1_col1_c'],
            ":wrat5pg1c1d": event['wide_range_achievement_test_5_pg1_col1_d'],
            ":wrat5pg1c1e": event['wide_range_achievement_test_5_pg1_col1_e']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wide_range_achievement_test_5_pg1_col2_a = :wrat5pg1c2a, wide_range_achievement_test_5_pg1_col2_b = :wrat5pg1c2b, wide_range_achievement_test_5_pg1_col2_c = :wrat5pg1c2c, wide_range_achievement_test_5_pg1_col2_d = :wrat5pg1c2d, wide_range_achievement_test_5_pg1_col2_e = :wrat5pg1c2e",
        ExpressionAttributeValues={
            ":wrat5pg1c2a": event['wide_range_achievement_test_5_pg1_col2_a'],
            ":wrat5pg1c2b": event['wide_range_achievement_test_5_pg1_col2_b'],
            ":wrat5pg1c2c": event['wide_range_achievement_test_5_pg1_col2_c'],
            ":wrat5pg1c2d": event['wide_range_achievement_test_5_pg1_col2_d'],
            ":wrat5pg1c2e": event['wide_range_achievement_test_5_pg1_col2_e']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wide_range_achievement_test_5_pg1_col3_a = :wrat5pg1c3a, wide_range_achievement_test_5_pg1_col3_b = :wrat5pg1c3b, wide_range_achievement_test_5_pg1_col3_c = :wrat5pg1c3c, wide_range_achievement_test_5_pg1_col3_d = :wrat5pg1c3d, wide_range_achievement_test_5_pg1_col3_e = :wrat5pg1c3e",
        ExpressionAttributeValues={
            ":wrat5pg1c3a": event['wide_range_achievement_test_5_pg1_col3_a'],
            ":wrat5pg1c3b": event['wide_range_achievement_test_5_pg1_col3_b'],
            ":wrat5pg1c3c": event['wide_range_achievement_test_5_pg1_col3_c'],
            ":wrat5pg1c3d": event['wide_range_achievement_test_5_pg1_col3_d'],
            ":wrat5pg1c3e": event['wide_range_achievement_test_5_pg1_col3_e']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
