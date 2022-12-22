from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('hrm/', include('hrm.urls')),
    path('user/', include('user.urls')),
    path('facial/recognition/', include('facialrecognition.urls')),
    path('supply/chain/', include('supplychain.urls')),
    path('machine/vision/', include('machinevision.urls')),
    path('', include('website.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)