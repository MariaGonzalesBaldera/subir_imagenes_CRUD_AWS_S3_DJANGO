import boto3

def create_folder(bucket, directory_name):
    try:
        s3 = boto3.client('s3')
        key = directory_name + '/'
        s3.put_object(Bucket=bucket, Key=key)
        return key

    except Exception as err:
        print(err)    

def upload_image(bucket, mediafile_key, file):
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket)

        return bucket.put_object(
            ACL = 'public-read',
            Key = mediafile_key,
            ContenType = file.content_type,
            Body = file
        ) 

    except Exception as err:
        print(err)