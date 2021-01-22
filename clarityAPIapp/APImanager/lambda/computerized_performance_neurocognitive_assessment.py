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
        UpdateExpression="SET computerized_performance_neurocognitive_assessment_a = :cpnaa, computerized_performance_neurocognitive_assessment_col1_a = :cpnacol1a, computerized_performance_neurocognitive_assessment_col1b = :cpnacol1b, computerized_performance_neurocognitive_assessment_col1_c = :cpnacol1c, computerized_performance_neurocognitive_assessment_col1_d = :cpnacol1d, computerized_performance_neurocognitive_assessment_col1_e = :cpnacol1e, computerized_performance_neurocognitive_assessment_col1_f = :cpnacol1f, computerized_performance_neurocognitive_assessment_col1_g = :cpnacol1g, computerized_performance_neurocognitive_assessment_col1_h = :cpnacol1h, computerized_performance_neurocognitive_assessment_col1_i = :cpnacol1i, computerized_performance_neurocognitive_assessment_col1_j = :cpnacol1j, computerized_performance_neurocognitive_assessment_col1_k = :cpnacol1k, computerized_performance_neurocognitive_assessment_col1_l = :cpnacol1l, computerized_performance_neurocognitive_assessment_col1_m = :cpnacol1m, computerized_performance_neurocognitive_assessment_col1_n = :cpnacol1n, computerized_performance_neurocognitive_assessment_col1_o = :cpnacol1o, computerized_performance_neurocognitive_assessment_col2_a = :cpnacol2a, computerized_performance_neurocognitive_assessment_col2_b = :cpnacol2b, computerized_performance_neurocognitive_assessment_col2_c = :cpnacol2c, computerized_performance_neurocognitive_assessment_col2_d = :cpnacol2d, computerized_performance_neurocognitive_assessment_col2_e = :cpnacol2e, computerized_performance_neurocognitive_assessment_col2_f = :cpnacol2f, computerized_performance_neurocognitive_assessment_col2_g = :cpnacol2g, computerized_performance_neurocognitive_assessment_col2_h = :cpnacol2h, computerized_performance_neurocognitive_assessment_col2_i = :cpnacol2i, computerized_performance_neurocognitive_assessment_col2_j = :cpnacol2j, computerized_performance_neurocognitive_assessment_col2_k = :cpnacol2k, computerized_performance_neurocognitive_assessment_col2_l = :cpnacol2l, computerized_performance_neurocognitive_assessment_col2_m = :cpnacol2m, computerized_performance_neurocognitive_assessment_col2_n = :cpnacol2n, computerized_performance_neurocognitive_assessment_col2_o = :cpnacol2o, computerized_performance_neurocognitive_assessment_col2_p = :cpnacol2p, computerized_performance_neurocognitive_assessment_col3_a = :cpnacol3a, computerized_performance_neurocognitive_assessment_col3_b = :cpnacol3b, computerized_performance_neurocognitive_assessment_col3_c = :cpnacol3c, computerized_performance_neurocognitive_assessment_col3_d = :cpnacol3d, computerized_performance_neurocognitive_assessment_col3_e = :cpnacol3e, computerized_performance_neurocognitive_assessment_col3_f = :cpnacol3f, computerized_performance_neurocognitive_assessment_col3_g = :cpnacol3g, computerized_performance_neurocognitive_assessment_col3_h = :cpnacol3h, computerized_performance_neurocognitive_assessment_col3_i = :cpnacol3i, computerized_performance_neurocognitive_assessment_col3_j = :cpnacol3j, computerized_performance_neurocognitive_assessment_col3_k = :cpnacol3k, computerized_performance_neurocognitive_assessment_col3_l = :cpnacol3l, computerized_performance_neurocognitive_assessment_col3_m = :cpnacol3m, computerized_performance_neurocognitive_assessment_col3_n = :cpnacol3n, computerized_performance_neurocognitive_assessment_col3_o = :cpnacol3o, computerized_performance_neurocognitive_assessment_col3_p = :cpnacol3p",
        ExpressionAttributeValues={
            ":cpnaa": event['computerized_performance_neurocognitive_assessment_a'],
            ":cpnacol1a": event['computerized_performance_neurocognitive_assessment_col1_a'],
            ":cpnacol1b": event['computerized_performance_neurocognitive_assessment_col1_b'],
            ":cpnacol1c": event['computerized_performance_neurocognitive_assessment_col1_c'],
            ":cpnacol1d": event['computerized_performance_neurocognitive_assessment_col1_d'],
            ":cpnacol1e": event['computerized_performance_neurocognitive_assessment_col1_e'],
            ":cpnacol1f": event['computerized_performance_neurocognitive_assessment_col1_f'],
            ":cpnacol1g": event['computerized_performance_neurocognitive_assessment_col1_g'],
            ":cpnacol1h": event['computerized_performance_neurocognitive_assessment_col1_h'],
            ":cpnacol1i": event['computerized_performance_neurocognitive_assessment_col1_i'],
            ":cpnacol1j": event['computerized_performance_neurocognitive_assessment_col1_j'],
            ":cpnacol1k": event['computerized_performance_neurocognitive_assessment_col1_k'],
            ":cpnacol1l": event['computerized_performance_neurocognitive_assessment_col1_l'],
            ":cpnacol1m": event['computerized_performance_neurocognitive_assessment_col1_m'],
            ":cpnacol1n": event['computerized_performance_neurocognitive_assessment_col1_n'],
            ":cpnacol1o": event['computerized_performance_neurocognitive_assessment_col1_o'],
            ":cpnacol1p": event['computerized_performance_neurocognitive_assessment_col1_p'],
            ":cpnacol2a": event['computerized_performance_neurocognitive_assessment_col2_a'],
            ":cpnacol2b": event['computerized_performance_neurocognitive_assessment_col2_b'],
            ":cpnacol2c": event['computerized_performance_neurocognitive_assessment_col2_c'],
            ":cpnacol2d": event['computerized_performance_neurocognitive_assessment_col2_d'],
            ":cpnacol2e": event['computerized_performance_neurocognitive_assessment_col2_e'],
            ":cpnacol2f": event['computerized_performance_neurocognitive_assessment_col2_f'],
            ":cpnacol2g": event['computerized_performance_neurocognitive_assessment_col2_g'],
            ":cpnacol2h": event['computerized_performance_neurocognitive_assessment_col2_h'],
            ":cpnacol2i": event['computerized_performance_neurocognitive_assessment_col2_i'],
            ":cpnacol2j": event['computerized_performance_neurocognitive_assessment_col2_j'],
            ":cpnacol2k": event['computerized_performance_neurocognitive_assessment_col2_k'],
            ":cpnacol2l": event['computerized_performance_neurocognitive_assessment_col2_l'],
            ":cpnacol2m": event['computerized_performance_neurocognitive_assessment_col2_m'],
            ":cpnacol2n": event['computerized_performance_neurocognitive_assessment_col2_n'],
            ":cpnacol2o": event['computerized_performance_neurocognitive_assessment_col2_o'],
            ":cpnacol2p": event['computerized_performance_neurocognitive_assessment_col2_p'],
            ":cpnacol3a": event['computerized_performance_neurocognitive_assessment_col3_a'],
            ":cpnacol3b": event['computerized_performance_neurocognitive_assessment_col3_b'],
            ":cpnacol3c": event['computerized_performance_neurocognitive_assessment_col3_c'],
            ":cpnacol3d": event['computerized_performance_neurocognitive_assessment_col3_d'],
            ":cpnacol3e": event['computerized_performance_neurocognitive_assessment_col3_e'],
            ":cpnacol3f": event['computerized_performance_neurocognitive_assessment_col3_f'],
            ":cpnacol3g": event['computerized_performance_neurocognitive_assessment_col3_g'],
            ":cpnacol3h": event['computerized_performance_neurocognitive_assessment_col3_h'],
            ":cpnacol3i": event['computerized_performance_neurocognitive_assessment_col3_i'],
            ":cpnacol3j": event['computerized_performance_neurocognitive_assessment_col3_j'],
            ":cpnacol3k": event['computerized_performance_neurocognitive_assessment_col3_k'],
            ":cpnacol3l": event['computerized_performance_neurocognitive_assessment_col3_l'],
            ":cpnacol3m": event['computerized_performance_neurocognitive_assessment_col3_m'],
            ":cpnacol3n": event['computerized_performance_neurocognitive_assessment_col3_n'],
            ":cpnacol3o": event['computerized_performance_neurocognitive_assessment_col3_o'],
            ":cpnacol3p": event['computerized_performance_neurocognitive_assessment_col3_p'],
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }


ds
