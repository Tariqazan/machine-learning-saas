from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.views.generic.base import TemplateView, View


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import *

from .utils import render_to_pdf

from django.core.mail import send_mail

import datetime

date = datetime.datetime.now()

# Create your views here.
class Dashboard(TemplateView):
    template_name = 'machinevision/dashboard.html'


class Products(TemplateView):
    template_name = 'machinevision/products.html'


class AssesmentProducts(TemplateView):
    template_name = 'machinevision/assessment_products.html'


class QualityInspection(TemplateView):
    template_name = 'machinevision/quality_inspection.html'


class GenerateMonthlyPdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'date': date
        }
        pdf = render_to_pdf('machinevision/pdf/monthly_pdf_counts.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GenerateWeeklyPdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'date': date
        }
        pdf = render_to_pdf('machinevision/pdf/weekly_pdf_counts.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GenerateDailyPdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'date': date
        }
        pdf = render_to_pdf('machinevision/pdf/daily_pdf_counts.html', data)
        return HttpResponse(pdf, content_type='application/pdf')