from django.urls import path
from .views import create

app_name='images'

urlpatterns =[
    path('create/', create, name='create')
]