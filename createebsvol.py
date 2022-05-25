# Create AWS EBS Volume Snapshot
import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1c',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-033b678cb085af161',
      VolumeType='gp2')
