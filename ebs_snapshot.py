#Create EBS snapshot
import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_snapshot( Description='snapshot from vol-03ca24e41cf224413', VolumeId='vol-03ca24e41cf224413')
