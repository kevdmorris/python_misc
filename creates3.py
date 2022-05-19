#create s3 bucket

import boto3

client = boto3.client("s3")
#bucket = s3.Bucket("kdm-bucket-test-boto3")
client.create_bucket(Bucket="kdm-bucket-test-boto3")
