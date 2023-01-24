import json
import boto3

def put_contact_index(event, context):
    dynamodb = boto3.client('dynamodb')
    #table = dynamodb.Table('usersTable1')
    req = json.loads(event["body"]) if type(event["body"]) == str else event["body"]
    res = dynamodb.update_item(
        TableName = "usersTable1",
        Key={
            'id':{"N": event["pathParameters"]["id"]}
        },
        
        ExpressionAttributeValues={
                ':lastname': {"S": req["lastname"]},
                ':firstname': {"S": req["firstname"]},
                ':email': {"S": req["email"]},              
                ':phone': {"S": req["phone"]},
                ':message': {"S": req["message"]},
                ':checkbox': {"BOOL": req["checkbox"]},
            },
        UpdateExpression = "SET lastname = :lastname, firstname = :firstname, email = :email, phone = :phone, message = :message,checkbox = :checkbox"
    )
    
    response = {
        "statusCode": 201,
        'body' : str(res) 
    }
    return response
    # body = {
    #     "id": event["pathParameters"]["id"],
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