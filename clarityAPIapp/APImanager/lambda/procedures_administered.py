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
        UpdateExpression="SET procedures_administered_pg1_a = :papg1a, procedures_administered_pg1_b = :papg1b, procedures_administered_pg1_c = :papg1c, procedures_administered_pg1_d = :papg1d, procedures_administered_pg1_e = :papg1e, procedures_administered_pg1_f = :papg1f, procedures_administered_pg1_g = :papg1g, procedures_administered_pg1_h = :papg1h, procedures_administered_pg1_i = :papg1i, procedures_administered_pg1_j = :papg1j, procedures_administered_pg1_k = :papg1k, procedures_administered_pg1_l = :papg1l, procedures_administered_pg1_m = :papg1m, procedures_administered_pg1_n = :papg1n, procedures_administered_pg1_o = :papg1o",
        ExpressionAttributeValues={
            ":papg1a": event['procedures_administered_pg1_a'],
            ":papg1b": event['procedures_administered_pg1_b'],
            ":papg1c": event['procedures_administered_pg1_c'],
            ":papg1d": event['procedures_administered_pg1_d'],
            ":papg1e": event['procedures_administered_pg1_e'],
            ":papg1f": event['procedures_administered_pg1_f'],
            ":papg1g": event['procedures_administered_pg1_g'],
            ":papg1h": event['procedures_administered_pg1_h'],
            ":papg1i": event['procedures_administered_pg1_i'],
            ":papg1j": event['procedures_administered_pg1_j'],
            ":papg1k": event['procedures_administered_pg1_k'],
            ":papg1l": event['procedures_administered_pg1_l'],
            ":papg1m": event['procedures_administered_pg1_m'],
            ":papg1n": event['procedures_administered_pg1_n'],
            ":papg1o": event['procedures_administered_pg1_o']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
