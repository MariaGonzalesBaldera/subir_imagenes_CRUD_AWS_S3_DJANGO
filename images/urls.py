from django.urls import path
from .views import create, update, show, delete, download

app_name='images'

urlpatterns =[
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('show/<int:pk>/', show, name='show'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('download/<int:pk>/', download, name='download'),

]