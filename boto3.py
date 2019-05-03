# python SDK to AWS

##### windows environment setting
# AWS_CONFIG_FILE  = C:\tmp\aws\config
[default]
region=us-east-1

# AWS_SHARED_CREDENTIALS_FILE = C:\tmp\aws\credentials
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
####


import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather')
print(table.creation_date_time)
