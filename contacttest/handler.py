import json
import boto3


dynamodb = boto3.resource('dynamodb')
table1 = dynamodb.Table('usersTable2')

def get(event, context):
    id = int(event["pathParameters"]["id"])
    res = table1.get_item(
        Key={
            'id': id,
        }
    )
    response = {
        "statusCode": 201,
        "body": str(res),
    }

    return response
    
 
def post(event, context):

    
        table_name1 = 'usersTable2'
        dynamodb1 = boto3.resource('dynamodb')
        if type(event["body"]) == str:
            req = json.loads(event["body"])
        else: 
            req = event["body"]
        res = dynamodb1.Table(table_name1).put_item(
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
        # body = {
        #     "message": event
        # }
        response = {
            "statusCode": 201,
              "body": str(res),
        }
        return response