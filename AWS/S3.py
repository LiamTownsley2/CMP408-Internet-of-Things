import boto3
import os

s3 = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

def upload_to_s3(file_path, bucket_name, object_name):
    s3.upload_file(file_path, bucket_name, object_name)