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
        UpdateExpression="SET neglect_abuse_trauma_loss_pg1_a = :natlpg1a, neglect_abuse_trauma_loss_pg1_b = :natlpg1b, neglect_abuse_trauma_loss_pg1_c = :natlpg1c",
        ExpressionAttributeValues={
            ":natlpg1a": event['neglect_abuse_trauma_loss_pg1_a'],
            ":natlpg1b": event['neglect_abuse_trauma_loss_pg1_b'],
            ":natlpg1c": event['neglect_abuse_trauma_loss_pg1_c']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET neglect_abuse_trauma_loss_pg2_a = :natlpg2a, neglect_abuse_trauma_loss_pg2_b = :natlpg2b, neglect_abuse_trauma_loss_pg2_c = :natlpg2c",
        ExpressionAttributeValues={
            ":natlpg2a": event['neglect_abuse_trauma_loss_pg2_a'],
            ":natlpg2b": event['neglect_abuse_trauma_loss_pg2_b'],
            ":natlpg2c": event['neglect_abuse_trauma_loss_pg2_c']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET neglect_abuse_trauma_loss_pg3_a = :natlpg3a, neglect_abuse_trauma_loss_pg3_b = :natlpg3b, neglect_abuse_trauma_loss_pg3_c = :natlpg3c",
        ExpressionAttributeValues={
            ":natlpg3a": event['neglect_abuse_trauma_loss_pg3_a'],
            ":natlpg3b": event['neglect_abuse_trauma_loss_pg3_b'],
            ":natlpg3c": event['neglect_abuse_trauma_loss_pg3_c']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET neglect_abuse_trauma_loss_pg4_a = :natlpg4a, neglect_abuse_trauma_loss_pg4_b = :natlpg4b, neglect_abuse_trauma_loss_pg4_c = :natlpg4c",
        ExpressionAttributeValues={
            ":natlpg4a": event['neglect_abuse_trauma_loss_pg4_a'],
            ":natlpg4b": event['neglect_abuse_trauma_loss_pg4_b'],
            ":natlpg4c": event['neglect_abuse_trauma_loss_pg4_c']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET neglect_abuse_trauma_loss_pg5_a = :natlpg5a, neglect_abuse_trauma_loss_pg5_b = :natlpg5b, neglect_abuse_trauma_loss_pg5_c = :natlpg5c",
        ExpressionAttributeValues={
            ":natlpg5a": event['neglect_abuse_trauma_loss_pg5_a'],
            ":natlpg5b": event['neglect_abuse_trauma_loss_pg5_b'],
            ":natlpg5c": event['neglect_abuse_trauma_loss_pg5_c']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps('That worked as it was supposed to.')
    }
