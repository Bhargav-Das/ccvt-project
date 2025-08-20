import boto3

aws_management_console = boto3.session.Session(profile_name="Bhargav")

ec2_console = aws_management_console.client(service_name="ec2", region_name="us-east-1")

response = ec2_console.run_instances(
    ImageId='ami-00a929b66ed6e0de6',  # Amazon Linux 2 AMI (HVM), SSD Volume Type
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'test55'  # Replace with your desired instance name
                }
            ]
        }
    ]
)
