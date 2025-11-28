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

    response = ec2.describe_instances(InstanceIds=[instance_id])
    public_ip = response["Reservations"][0]["Instances"][0]["PublicIpAddress"]

    print(f"Staging server is now running at: {public_ip}")

    github_output = os.environ["GITHUB_OUTPUT"]
    with open(github_output, "a") as f:
        f.write(f"public_ip={public_ip}\n")

if __name__ == "__main__":
    main()
