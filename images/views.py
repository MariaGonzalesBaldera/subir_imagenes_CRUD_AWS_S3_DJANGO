from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from .forms import UploadFileForm
from .models import Image, Album
from AWS import upload_image,delete_mediafile, get_mediafile_content
from django.conf import settings

def download(request, pk):
    image = get_object_or_404(Image, pk= pk)
    content = get_mediafile_content(image.bucket, image.key)
    response = HttpResponse(content, content_type=image.content_type)
    response['Content-Disposition'] = f'attachment; filename={image.name}'
    return response 

def show(request, pk):

    image = get_object_or_404(Image, pk=pk)
    return JsonResponse({
        'id': image.id,
        'name': image.name,
        'delete_url': reverse('images:delete', kwargs={'pk':image.id})
    })

def update(request, pk):
    image = get_object_or_404(Image, pk=pk)

    if request.method == 'POST':
        new_name = request.POST.get('name','')
        image.set_name(new_name)

    return JsonResponse({
        'id':image.id,
        'name':image.title,
        'url':image.url
    })

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST , request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            album = get_object_or_404(Album, id= form.cleaned_data['album_id'])

            key = album.key + file._name
            if upload_image(settings.BUCKET , key, file):


                image = Image.objects.create(
                    name = file._name,
                    content_type = file.content_type,
                    size = file.size,
                    bucket = settings.BUCKET,
                    key = key,
                    album = album
                )

            return redirect('albums:detail', album.id)
        
def delete(request, pk):
    image = get_object_or_404(Image, pk=pk)
    album = image.album
    if(delete_mediafile(image.bucket, image.key)):
        image.delete()

    return redirect('albums:detail', album.id)