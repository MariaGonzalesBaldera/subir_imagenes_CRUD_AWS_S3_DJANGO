from django.shortcuts import render, redirect
from .forms import UploadFileForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST , request.FILES)
        if form.is_valid():
            image = form.cleaned_data['file']

            print(image)    
            print(image.__dict__)
            return redirect('albums:list')