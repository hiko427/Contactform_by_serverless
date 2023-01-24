import json
def test(event, context):
    
    response = {
        "statusCode": 201,
        "body": json.dumps(event)
    }
    return response