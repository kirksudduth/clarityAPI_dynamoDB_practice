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
        UpdateExpression="SET rorschach_performance_assessment_system_pg1_a = :rpaspg1a",
        ExpressionAttributeValues={
            ":rpaspg1a": event['rorschach_performance_assessment_system_pg1_a']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
