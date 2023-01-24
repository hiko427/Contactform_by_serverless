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

def put_contact_index(event, context):
    dynamodb = boto3.client('dynamodb')
    req = event["body"]
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
