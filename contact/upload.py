import json
import boto3
import base64
from datetime import datetime
BUCKET_NAME='buckettsubasatest'

s3 = boto3.resource('s3')

def upload(event, context):
    bucket = s3.Bucket(BUCKET_NAME)
    
    body = base64.b64decode(event['body']) if event['headers']['Content-Type'] == "image/png" else event['body']
 
    key = str(datetime.now())+ ".png" if event['headers']['Content-Type'] == "image/png" else str(datetime.now())+ ".txt"
    
    bucket.put_object(Body=body, Key=key)

    return {
        'statusCode': 200,
        'body': json.dumps('アップロード完了')
    }