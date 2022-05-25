#Remove VPC
import boto3
client=boto3.client("ec2")
client.delete_vpc(VpcId='vpc-00ed47c6cfae7581e')


