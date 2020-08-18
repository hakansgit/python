import boto3

# use aws s3
s3 = boto3.resource('s3')

# list all buckets
for bucket in s3.buckets.all():
    print(bucket.name)

# upload a file
file = open('test.py', 'rb')
s3.Bucket('my-website-20180602').put_object(Key='test.py', Body=file)

