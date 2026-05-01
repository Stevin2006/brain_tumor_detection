from django.urls import path
from . import views

urlpatterns = [
    # This makes the upload page the 'home' of this app
    path('', views.upload_mri, name='upload_mri'),
]