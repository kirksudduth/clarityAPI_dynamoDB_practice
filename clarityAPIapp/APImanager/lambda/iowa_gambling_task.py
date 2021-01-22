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
        UpdateExpression="SET iowa_gambling_task_a = :igta, iowa_gambling_task_b = :igtb, iowa_gambling_task_c = :igtc",
        ExpressionAttributeValues={
            ":igta": event['iowa_gambling_task_a'],
            ":igtb": event['iowa_gambling_task_b'],
            ":igtc": event['iowa_gambling_task_c']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
