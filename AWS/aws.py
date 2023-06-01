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
            ContentType = file.content_type,
            Body = file
        ) 

    except Exception as err:
        print(err)
def rename_file(bucket, new_media_file_name, old_media_file_name):
    try:
        s3 = boto3.resource('s3')
        
        s3.Object(bucket, new_media_file_name).copy_from(CopySource = bucket+'/'+old_media_file_name)
        s3.Object(bucket, old_media_file_name).delete()

        s3.Object(bucket, new_media_file_name).Acl().put(ACL='public-read')

        return True

    except Exception as err:
        print(err)

def delete_mediafile(bucket, mediafile_key):
    try:
        s3 = boto3.resource('s3')
        s3.Object(bucket, mediafile_key).delete()
        return True

    except Exception as err:
        print(err)        

def get_mediafile_content(bucket, mediafile_key):
    try:
        s3 = boto3.client('s3')
        data = s3.get_object(Bucket = bucket, Key= mediafile_key)
        return data['Body'].read()

    except Exception as err:
        print(err)        
