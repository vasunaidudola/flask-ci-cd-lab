import os
import boto3

def main():
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
    secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    region = os.environ["AWS_DEFAULT_REGION"]
    instance_id = os.environ["STAGING_INSTANCE_ID"]

    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region,
    )

    print(f"Stopping staging instance: {instance_id}")
    ec2.stop_instances(InstanceIds=[instance_id])

if __name__ == "__main__":
    main()
