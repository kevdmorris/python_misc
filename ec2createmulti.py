# Create multiple EC2 instances

import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-0022f774911c1d690',
      InstanceType='t2.micro',
    MaxCount=4,
      MinCount=3)

