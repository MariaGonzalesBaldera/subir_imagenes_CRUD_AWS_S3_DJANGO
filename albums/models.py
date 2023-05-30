from django.db import models
from AWS import create_folder

class AlbumManager(models.Manager):
    def create_by_aws(self, bucket, title, description):
        key = title.replace(' ','_').lower()

        if create_folder(bucket,key) :
            return self.create(title=title, 
                               description=description, 
                               bucket=bucket, 
                               key=key)

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50,null=False, blank=False)
    description = models.TextField()
    bucket = models.CharField(max_length=100,null=False, blank=False)
    key = models.CharField(max_length=100,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AlbumManager()

    def __str__(self) :
        return self.title
    