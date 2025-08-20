import boto3

# Initialize the S3 client
s3 = boto3.client('s3', region_name='us-east-1')  # Replace 'us-east-1' with your desired region

# Create the S3 bucket
response = s3.create_bucket(
    Bucket='bhargav-bucket-12345678900'  # Replace with your desired bucket name
)

print("Bucket created successfully:", response)

# Bucket = 'bhargav-bucket-123456789'  # Replace with your desired bucket name

# file_name = 'story.jpg '  # Replace with your file name

# s3.upload_file(file_name, Bucket, file_name)
# print("File uploaded successfully:", file_name)

# s3.download_file(Bucket, file_name, 'downloaded_' + file_name)
# print("File downloaded successfully:", file_name)

# s3.delete_object(Bucket=Bucket, Key=file_name)
# print("File deleted successfully:", file_name)

