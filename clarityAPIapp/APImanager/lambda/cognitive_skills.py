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
        UpdateExpression="SET cognitive_skills_pg1_a = :cspg1a, cognitive_skills_pg1_b = :cspg1b, cognitive_skills_pg1_c = :cspg1c, cognitive_skills_pg1_d = :cspg1d",
        ExpressionAttributeValues={
            ":cspg1a": event['cognitive_skills_pg1_a'],
            ":cspg1b": event['cognitive_skills_pg1_b'],
            ":cspg1c": event['cognitive_skills_pg1_c'],
            ":cspg1d": event['cognitive_skills_pg1_d']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
