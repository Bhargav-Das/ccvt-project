import boto3

# Initialize the S3 client
s3 = boto3.client('s3', region_name='us-east-1')  # Replace 'us-east-1' with your desired region

# Create the S3 bucket
response = s3.create_bucket(
    Bucket='bhargav-bucket-123456789'  # Replace with your desired bucket name
)

print("Bucket created successfully:", response)