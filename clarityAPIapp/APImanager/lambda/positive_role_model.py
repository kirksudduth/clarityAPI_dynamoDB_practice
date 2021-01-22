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
        UpdateExpression="SET positive_role_model_pg1_a = :prmpg1a, positive_role_model_pg1_b = :prmpg1b, positive_role_model_pg1_c = :prmpg1c, positive_role_model_pg1_d = :prmpg1d, positive_role_model_pg1_e = :prmpg1e, positive_role_model_pg1_f = :prmpg1f, positive_role_model_pg1_g = :prmpg1g, positive_role_model_pg1_h = :prmpg1h, positive_role_model_pg1_i = :prmpg1i",
        ExpressionAttributeValues={
            ":prmpg1a": event['positive_role_model_pg1_a'],
            ":prmpg1b": event['positive_role_model_pg1_b'],
            ":prmpg1c": event['positive_role_model_pg1_c'],
            ":prmpg1d": event['positive_role_model_pg1_d'],
            ":prmpg1e": event['positive_role_model_pg1_e'],
            ":prmpg1f": event['positive_role_model_pg1_f'],
            ":prmpg1g": event['positive_role_model_pg1_g'],
            ":prmpg1h": event['positive_role_model_pg1_h'],
            ":prmpg1i": event['positive_role_model_pg1_i'],
            ":prmpg1j": event['positive_role_model_pg1_j']
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
        UpdateExpression="SET positive_role_model_pg2_a = :prmpg2a, positive_role_model_pg2_b = :prmpg2b, positive_role_model_pg2_c = :prmpg2c, positive_role_model_pg2_d = :prmpg2d, positive_role_model_pg2_e = :prmpg2e, positive_role_model_pg2_f = :prmpg2f, positive_role_model_pg2_g = :prmpg2g",
        ExpressionAttributeValues={
            ":prmpg2a": event['positive_role_model_pg2_a'],
            ":prmpg2b": event['positive_role_model_pg2_b'],
            ":prmpg2c": event['positive_role_model_pg2_c'],
            ":prmpg2d": event['positive_role_model_pg2_d'],
            ":prmpg2e": event['positive_role_model_pg2_e'],
            ":prmpg2f": event['positive_role_model_pg2_f'],
            ":prmpg2g": event['positive_role_model_pg2_g']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
