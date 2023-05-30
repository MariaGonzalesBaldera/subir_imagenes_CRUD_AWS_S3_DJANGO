from django.db import models
from albums.models import Album

# Create your models here.
class Image(models.Model):
    key = models.CharField(max_length=100, null=False, blank=False)
    bucket = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    content_type = models.CharField(max_length=20, null=False, blank=False)
    size = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name