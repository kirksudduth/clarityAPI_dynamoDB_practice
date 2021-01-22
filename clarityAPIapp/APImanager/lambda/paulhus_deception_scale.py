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
        UpdateExpression="SET paulhus_deception_scale_a = :pdsa, paulhus_deception_scale_b = :pdsb, paulhus_deception_scale_c = :pdsc, paulhus_deception_scale_d = :pdsd",
        ExpressionAttributeValues={
            ":pdsa": event['paulhus_deception_scale_a'],
            ":pdsb": event['paulhus_deception_scale_b'],
            ":pdsc": event['paulhus_deception_scale_c'],
            ":pdsd": event['paulhus_deception_scale_d']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
