import boto3

def create_folder(bucket, directory_name):
    try:
        s3 = boto3.client('s3')
        key = directory_name + '/'
        s3.put_object(Bucket=bucket, Key=key)
        return key

    except Exception as err:
        print(err)    
