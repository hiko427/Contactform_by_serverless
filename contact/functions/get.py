import json
import boto3

def get_contact_index(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('usersTable1')
    
    res = table.get_item(
        Key={
            'id': int(event["pathParameters"]["id"])
        }
    )
    response = {
        "statusCode": 200,
        'body' : str(res) 
    }
    return response

# get_contact_index()
    # body = {
    #     "id": event["pathParameters"]["id"],
    #     "lastname" : "last name",
    #     "firstname" : "first name",
    #     "email" : "email",
    #     "phone" : "phone number",
    #     "message" : "message",
    #     "checkbox" : True,
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response