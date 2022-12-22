from django.urls import path
from .views import *

urlpatterns = [
    path('', FacialRecognition.as_view(),
         name="facial_recognition"),
]
