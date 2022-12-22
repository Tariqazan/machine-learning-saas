from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import *
# Create your views here.


class SignUp(CreateView):
    form_class = UserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')