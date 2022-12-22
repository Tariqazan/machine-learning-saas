from django.urls import path
from .views import *

urlpatterns = [
      path('dashboard/', Dashboard.as_view(), name="machine_vision"),
    path('products/', Products.as_view(), name="products"),
    path('assessment/products/', AssesmentProducts.as_view(), name="assessment_products"),
    path("quality/inspection/", QualityInspection.as_view(), name="quality_inspection"),
    path('monthly/count/data/pdf/', GenerateMonthlyPdf.as_view(),
         name="monthly_count_data_pdf"),
    path('weekly/count/data/pdf/', GenerateWeeklyPdf.as_view(),
         name="weekly_count_data_pdf"),
    path('daily/count/data/pdf/', GenerateDailyPdf.as_view(),
         name="daily_count_data_pdf"),
]
