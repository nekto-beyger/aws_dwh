import boto3
from botocore.exceptions import ClientError

s3c = boto3.client('s3')
s3r = boto3.resource('s3')

for bucket in s3r.buckets.all():
    try: 
       
        bckt_version = s3r.BucketVersioning(bucket.name)
        if bckt_version.status == 'Enabled':
            bucket.object_versions.delete()
        else:
            bucket.objects.all().delete() #bucket clean 
            
        s3c.delete_bucket(Bucket = bucket.name) #delete bucket
    except ClientError as e:
        print('Error: ', e)
        