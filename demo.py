import boto3

# Initialize the S3 client
client = boto3.client('s3', region_name='ap-south-1')  # Replace 'your-region' with the region where the bucket was created

# Specify the bucket name
bucket_name = 'newpb3bkt',  # Replace 'your-bucket-name' with the name of your bucket

# Delete the bucket
def delete_empty_bucket(newpb3bkt):
    try:
        client.delete_bucket(newpb3bkt)
        print(f"Bucket '{newpb3bkt}' deleted successfully!")
    except Exception as e:
        print(f"Error deleting bucket: {e}")

# Call the function to delete the bucket
delete_empty_bucket(newpb3bkt)

