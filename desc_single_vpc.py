# Describe a single vpc based on VpcId
import boto3
client=boto3.client("ec2")
x=client.describe_vpcs(VpcIds=["vpc-0939244b5ef44e4bb"])
#no_of_vpcs=x["Vpcs"]
#len (no_of_vpcs)
#print(no_of_vpcs)
#for vpc in no_of_vpcs:
#print(VpcIds=["vpc-0939244b5ef44e4bb"])
