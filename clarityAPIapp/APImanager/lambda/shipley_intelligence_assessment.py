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
        UpdateExpression="SET shipley_intelligence_assessment_2_pg1_col1_a = :sis2pg1c1a, shipley_intelligence_assessment_2_pg1_col1_b = :sis2pg1c1b, shipley_intelligence_assessment_2_pg1_col1_c = :sis2pg1c1c, shipley_intelligence_assessment_2_pg1_col1_d = :sis2pg1c1d, shipley_intelligence_assessment_2_pg1_col1_e = :sis2pg1c1e, shipley_intelligence_assessment_2_pg1_col1_f = :sis2pg1c1f",
        ExpressionAttributeValues={
            ":sis2pg1c1a": event['shipley_intelligence_assessment_2_pg1_col1_a'],
            ":sis2pg1c1b": event['shipley_intelligence_assessment_2_pg1_col1_b'],
            ":sis2pg1c1c": event['shipley_intelligence_assessment_2_pg1_col1_c'],
            ":sis2pg1c1d": event['shipley_intelligence_assessment_2_pg1_col1_d'],
            ":sis2pg1c1e": event['shipley_intelligence_assessment_2_pg1_col1_e'],
            ":sis2pg1c1f": event['shipley_intelligence_assessment_2_pg1_col1_f']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET shipley_intelligence_assessment_2_pg1_col2_a = :sis2pg1c2a, shipley_intelligence_assessment_2_pg1_col2_b = :sis2pg1c2b, shipley_intelligence_assessment_2_pg1_col2_c = :sis2pg1c2c, shipley_intelligence_assessment_2_pg1_col2_d = :sis2pg1c2d, shipley_intelligence_assessment_2_pg1_col2_e = :sis2pg1c2e, shipley_intelligence_assessment_2_pg1_col2_f = :sis2pg1c2f",
        ExpressionAttributeValues={
            ":sis2pg1c2a": event['shipley_intelligence_assessment_2_pg1_col2_a'],
            ":sis2pg1c2b": event['shipley_intelligence_assessment_2_pg1_col2_b'],
            ":sis2pg1c2c": event['shipley_intelligence_assessment_2_pg1_col2_c'],
            ":sis2pg1c2d": event['shipley_intelligence_assessment_2_pg1_col2_d'],
            ":sis2pg1c2e": event['shipley_intelligence_assessment_2_pg1_col2_e'],
            ":sis2pg1c2f": event['shipley_intelligence_assessment_2_pg1_col2_f']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
