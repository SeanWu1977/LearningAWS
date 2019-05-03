# python SDK to AWS
pip install boto3

##### linux
~/.aws/config
~/.aws/credentials

##### windows environment setting
# AWS_CONFIG_FILE  = C:\tmp\aws\config
# AWS_SHARED_CREDENTIALS_FILE = C:\tmp\aws\credentials

# config file
[default]
region=us-east-1

# credentials file
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY




### python program ###
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather')
print(table.creation_date_time)
