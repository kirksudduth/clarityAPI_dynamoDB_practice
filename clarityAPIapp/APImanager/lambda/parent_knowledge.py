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
        UpdateExpression="SET parent_knowledge_pg1_a = :pkpg1a, parent_knowledge_pg1_b = :pkpg1b, parent_knowledge_pg1_c = :pkpg1c, parent_knowledge_pg1_d = :pkpg1d, parent_knowledge_pg1_e = :pkpg1e, parent_knowledge_pg1_f = :pkpg1f, parent_knowledge_pg1_g = :pkpg1g, parent_knowledge_pg1_h = :pkpg1h, parent_knowledge_pg1_i = :pkpg1i",
        ExpressionAttributeValues={
            ":pkpg1a": event['parent_knowledge_pg1_a'],
            ":pkpg1b": event['parent_knowledge_pg1_b'],
            ":pkpg1c": event['parent_knowledge_pg1_c'],
            ":pkpg1c": event['parent_knowledge_pg1_d'],
            ":pkpg1c": event['parent_knowledge_pg1_e'],
            ":pkpg1c": event['parent_knowledge_pg1_f'],
            ":pkpg1c": event['parent_knowledge_pg1_g'],
            ":pkpg1c": event['parent_knowledge_pg1_h'],
            ":pkpg1c": event['parent_knowledge_pg1_i']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
