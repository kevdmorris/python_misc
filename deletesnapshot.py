#Create EBS snapshot
import boto3
ec2_client=boto3.client("ec2")
ec2_client.delete_snapshot(SnapshotId='snap-033b678cb085af161')
