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
        UpdateExpression="SET wechsler_adult_intelligence_scale_IV_pg1_col1_a = :waispg1c1a, wechsler_adult_intelligence_scale_IV_pg1_col1_b = :waispg1c1b, wechsler_adult_intelligence_scale_IV_pg1_col1_c = :waispg1c1c, wechsler_adult_intelligence_scale_IV_pg1_col1_d = :waispg1c1d, wechsler_adult_intelligence_scale_IV_pg1_col1_e = :waispg1c1e",
        ExpressionAttributeValues={
            ":waispg1c1a": event['wechsler_adult_intelligence_scale_IV_pg1_col1_a'],
            ":waispg1c1b": event['wechsler_adult_intelligence_scale_IV_pg1_col1_b'],
            ":waispg1c1c": event['wechsler_adult_intelligence_scale_IV_pg1_col1_c'],
            ":waispg1c1d": event['wechsler_adult_intelligence_scale_IV_pg1_col1_d'],
            ":waispg1c1e": event['wechsler_adult_intelligence_scale_IV_pg1_col1_e']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wechsler_adult_intelligence_scale_IV_pg1_col2_a = :waispg1c2a, wechsler_adult_intelligence_scale_IV_pg1_col2_b = :waispg1c2b, wechsler_adult_intelligence_scale_IV_pg1_col2_c = :waispg1c2c, wechsler_adult_intelligence_scale_IV_pg1_col2_d = :waispg1c2d, wechsler_adult_intelligence_scale_IV_pg1_col2_e = :waispg1c2e",
        ExpressionAttributeValues={
            ":waispg1c2a": event['wechsler_adult_intelligence_scale_IV_pg1_col2_a'],
            ":waispg1c2b": event['wechsler_adult_intelligence_scale_IV_pg1_col2_b'],
            ":waispg1c2c": event['wechsler_adult_intelligence_scale_IV_pg1_col2_c'],
            ":waispg1c2d": event['wechsler_adult_intelligence_scale_IV_pg1_col2_d'],
            ":waispg1c2e": event['wechsler_adult_intelligence_scale_IV_pg1_col2_e']
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
        UpdateExpression="SET wechsler_adult_intelligence_scale_IV_pg2_col1_a = :waispg2c1a, wechsler_adult_intelligence_scale_IV_pg2_col1_b = :waispg2c1b, wechsler_adult_intelligence_scale_IV_pg2_col1_c = :waispg2c1c",
        ExpressionAttributeValues={
            ":waispg2c1a": event['wechsler_adult_intelligence_scale_IV_pg2_col1_a'],
            ":waispg2c1b": event['wechsler_adult_intelligence_scale_IV_pg2_col1_b'],
            ":waispg2c1c": event['wechsler_adult_intelligence_scale_IV_pg2_col1_c']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wechsler_adult_intelligence_scale_IV_pg2_col2_a = :waispg2c2a, wechsler_adult_intelligence_scale_IV_pg2_col2_b = :waispg2c2b, wechsler_adult_intelligence_scale_IV_pg2_col2_c = :waispg2c2c",
        ExpressionAttributeValues={
            ":waispg2c2a": event['wechsler_adult_intelligence_scale_IV_pg2_col2_a'],
            ":waispg2c2b": event['wechsler_adult_intelligence_scale_IV_pg2_col2_b'],
            ":waispg2c2c": event['wechsler_adult_intelligence_scale_IV_pg2_col2_c']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wechsler_adult_intelligence_scale_IV_pg2_col3_a = :waispg2c3a, wechsler_adult_intelligence_scale_IV_pg2_col3_b = :waispg2c3b, wechsler_adult_intelligence_scale_IV_pg2_col3_c = :waispg2c3c",
        ExpressionAttributeValues={
            ":waispg2c3a": event['wechsler_adult_intelligence_scale_IV_pg2_col3_a'],
            ":waispg2c3b": event['wechsler_adult_intelligence_scale_IV_pg2_col3_b'],
            ":waispg2c3c": event['wechsler_adult_intelligence_scale_IV_pg2_col3_c']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wechsler_adult_intelligence_scale_IV_pg2_col4_a = :waispg2c4a, wechsler_adult_intelligence_scale_IV_pg2_col4_b = :waispg2c4b, wechsler_adult_intelligence_scale_IV_pg2_col4_c = :waispg2c4c",
        ExpressionAttributeValues={
            ":waispg2c4a": event['wechsler_adult_intelligence_scale_IV_pg2_col4_a'],
            ":waispg2c4b": event['wechsler_adult_intelligence_scale_IV_pg2_col4_b'],
            ":waispg2c4c": event['wechsler_adult_intelligence_scale_IV_pg2_col4_c']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET wechsler_adult_intelligence_scale_IV_pg2_col5_a = :waispg2c5a, wechsler_adult_intelligence_scale_IV_pg2_col5_b = :waispg2c5b, wechsler_adult_intelligence_scale_IV_pg2_col5_c = :waispg2c5c",
        ExpressionAttributeValues={
            ":waispg2c5a": event['wechsler_adult_intelligence_scale_IV_pg2_col5_a'],
            ":waispg2c5b": event['wechsler_adult_intelligence_scale_IV_pg2_col5_b'],
            ":waispg2c5c": event['wechsler_adult_intelligence_scale_IV_pg2_col5_c']
        },
        ReturnValues="UPDATED_NEW")

    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
