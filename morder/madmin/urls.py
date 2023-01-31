from django.urls import path
from . import viewsAdmin


urlpatterns = [
    path("", viewsAdmin.index, name="shopHome"),
    
]