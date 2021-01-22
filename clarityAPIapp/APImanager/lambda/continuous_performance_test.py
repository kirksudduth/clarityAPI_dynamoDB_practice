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
        UpdateExpression="SET continuous_performance_test_3rd_ed_a = :cpta, continuous_performance_test_3rd_ed_b = :cptb, continuous_performance_test_3rd_ed_c = :cptc, continuous_performance_test_3rd_ed_d = :cptd",
        ExpressionAttributeValues={
            ":cpta": event['continuous_performance_test_3rd_ed_a'],
            ":cptb": event['continuous_performance_test_3rd_ed_b'],
            ":cptc": event['continuous_performance_test_3rd_ed_c'],
            ":cptd": event['continuous_performance_test_3rd_ed_d']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
