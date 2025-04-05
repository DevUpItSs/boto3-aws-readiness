# Boto3 AWS Readiness Example

import boto3

def check_instance_status(region_name="us-east-1"):
    ec2 = boto3.client('ec2', region_name=region_name)
    response = ec2.describe_instance_status(IncludeAllInstances=True)

    for instance in response['InstanceStatuses']:
        instance_id = instance['InstanceId']
        state = instance['InstanceState']['Name']
        status = instance['InstanceStatus']['Status']
        print(f"Instance ID: {instance_id}, State: {state}, Status: {status}")

if __name__ == "__main__":
    check_instance_status()
