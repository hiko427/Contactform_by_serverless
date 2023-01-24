import json
import boto3

def post_contact_index(event, context):
    table_name = 'usersTable1'
    dynamodb = boto3.resource('dynamodb')
    req = json.loads(event["body"]) if type(event["body"]) == str else event["body"]
    res = dynamodb.Table(table_name).put_item(
        Item={
            "id": req["id"],
            "lastname": req["lastname"],
            "firstname": req["firstname"],
            "email": req["email"],
            "phone": req["phone"],
            "message":req["message"],
            "checkbox":req["checkbox"]
        }   
    )
    response = {
        "statusCode": 201,
        'body' : str(res) 
    }
    return response




    # body = {
    #     "id": 1,
    #     "lastname" : "last name",
    #     "firstname" : "first name",
    #     "email" : "email",
    #     "phone" : "phone number",
    #     "message" : "message",
    #     "checkbox" : True
    # }
    # response = {
    #     "statusCode": 201,
    #     "body": json.dumps(body)
    # }
    # return response

