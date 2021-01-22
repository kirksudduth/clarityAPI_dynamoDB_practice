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
        UpdateExpression="SET material_resources_pg1_a = :mrpg1a, material_resources_pg1_b = :mrpg1b, material_resources_pg1_c = :mrpg1c, material_resources_pg1_d = :mrpg1d, material_resources_pg1_e = :mrpg1e, material_resources_pg1_f = :mrpg1f",
        ExpressionAttributeValues={
            ":mrpg1a": event['material_resources_pg1_a'],
            ":mrpg1b": event['material_resources_pg1_b'],
            ":mrpg1c": event['material_resources_pg1_c'],
            ":mrpg1d": event['material_resources_pg1_d'],
            ":mrpg1e": event['material_resources_pg1_e'],
            ":mrpg1f": event['material_resources_pg1_f']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
