from django.shortcuts import render
from django.views.generic.base import TemplateView
import requests

# Create your views here.

class FacialRecognition(TemplateView):
    template_name = 'facial_recognition/facial_recognition.html'

    def get(self,request):
        data = requests.get('http://192.168.1.16:5000/')
        # print(data.json())
        return render(request,self.template_name)