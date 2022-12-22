from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .models import *
from .sitemaps import BlogSitemap, CVSitemap

sitemaps = {
    'blog': BlogSitemap,
     'cv' : CVSitemap
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
         
    path('', Index.as_view(), name="index"),

    path('machine-vision-system/', MachineVisionSystem.as_view(),
         name="machine_vision_system"),
    path('performance-manufacturing/', PerformanceManufacturing.as_view(),
         name="manufacturing_execution_system"),
    path('indutrial-iot-4.0/', IndustrialIot.as_view(), name="IndustrialIot"),
    path("intelligence-supply-chain-management/",
         SupplyChainService.as_view(), name="supply_chain_service"),
    path("textile-4.0/", Textile.as_view(), name="textile"),

    path('About/', About.as_view(), name="about"),

    path('career/', Career.as_view(), name="career"),

    path('blogs/', Blogs.as_view(), name="blog"),

    path('add/blog/', CreateBlog.as_view(), name='create_blog'),
    path("blogs/list/", BlogListView.as_view(), name="blog_list"),
    path("blog/detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),

    path("subscription/", Subscription.as_view(), name="subscription"),

    path("post/cv/", PostCV.as_view(), name="postCV"),

    path("contact/post/", PostContact.as_view(),name='post_contact')
]
