# Get EC2 Instance ID's
import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"][0]
data_instance=data["Instances"]
for i in range (len(data_instance)):
    print (data_instance[i]) # verbose data_instance info
    #print(f"instance id is {data_instance[i]['InstanceId']}")
    


