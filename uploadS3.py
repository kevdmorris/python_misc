#Upload file to S3

import boto3

#upload single file
#s3_resource=boto3.client("s3")

#s3_resource.upload_file(
   # Filename="upload_test.sh",
    #Bucket="kdm-bucket-test-boto3",
    #Key="upload_test.sh")


import os
import glob

cwd=os.getcwd()
cwd=cwd="/home/ec2-user/environment/"

files=glob.glob(cwd+"*.sh")

#print(files)

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="kdm-bucket-test-boto3",
    Key=file.split("/") )

    files[0].split("/")
