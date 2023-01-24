import json
import boto3

def delete_contact_index(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('usersTable1')
    res = table.delete_item(
        Key={
            'id': int(event["pathParameters"]["id"])
        }
    )
    response = {
        "statusCode": 200,
        'body' : str(res) 
    }
    return response

    # body = {"message": "good request"}

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response