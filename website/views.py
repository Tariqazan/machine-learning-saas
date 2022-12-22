from django.db import models
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from website.models import Blog, Contact
from website.serializers import BlogSerializer, CareerCVSerializer, ContactSerializer
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return redirect('login')


class Industries(TemplateView):
    template_name = 'index.html'


class AssetManagementSystem(TemplateView):
    template_name = 'index.html'


class RemoteOperationDesign(TemplateView):
    template_name = 'index.html'


class SystemIntegration(TemplateView):
    template_name = 'index.html'


class MachineVisionSystem(TemplateView):
    template_name = 'index.html'


class FeasibilityStudies(TemplateView):
    template_name = 'index.html'


class PerformanceManufacturing(TemplateView):
    template_name = 'index.html'


class EducationTraining(TemplateView):
    template_name = 'index.html'


class ObjectDetection(TemplateView):
    template_name = 'index.html'


class Textile(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'index.html'


class IndustrialIot(TemplateView):
    template_name = 'index.html'


class Career(TemplateView):
    template_name = 'index.html'


class SupplyChain(TemplateView):
    template_name = 'index.html'


class Blogs(TemplateView):
    template_name = 'index.html'


class SupplyChainService(TemplateView):
    template_name = 'index.html'


class WorkForce(TemplateView):
    template_name = 'index.html'


class Dispatch(TemplateView):
    template_name = 'index.html'


class Asset(TemplateView):
    template_name = 'index.html'


class Subscription(TemplateView):
    template_name = 'subscription/subscription.html'


class CreateBlog(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/create_blog.html'
    success_url = '/blogs/'


class BlogListView(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all().order_by('-id')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogDetailView(APIView):
    def get(self, request, pk, format=None):
        blog = Blog.objects.get(id=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)


class PostCV(APIView):

    def post(self,request):
        cv = CareerCVSerializer(data=request.data)
        if cv.is_valid():
            cv.save()
            return Response(cv.data, status=status.HTTP_201_CREATED)
        else:
            print('error', cv.errors)
            return Response(cv.errors, status=status.HTTP_400_BAD_REQUEST)



class PostContact(APIView):
    def post(self,request):
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
            return Response(contact.data,status=status.HTTP_201_CREATED)
        else:
            print('error',contact.errors)
            return Response(contact.errors,status=status.HTTP_400_BAD_REQUEST)