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
        UpdateExpression="SET minnesota_multiphasic_personality_inventory_2_a = :mmpi2a, minnesota_multiphasic_personality_inventory_2_b = :mmpi2b",
        ExpressionAttributeValues={
            ":mmpi2a": event['minnesota_multiphasic_personality_inventory_2_a'],
            ":mmpi2b": event['minnesota_multiphasic_personality_inventory_2_b']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
