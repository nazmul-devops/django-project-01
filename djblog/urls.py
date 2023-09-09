from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from dbpost import urls as dbpost_urls
from djblog import settings
from django.urls import re_path


urlpatterns = [
    path('', lambda request: HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To Django Blog Project's Home Page.</h1>", content_type="text/html")),
    path("admin/", admin.site.urls),
    path("api/", include(dbpost_urls, namespace='dbpost')),
    # path('', include('admin_soft.urls')),
    # path('', include('admin_material.urls')),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

admin.site.site_title = "DJ Blog Admin Portal"
admin.site.site_header = "DJ Blog Admin"
admin.site.index_title = "Welcome to Django Blog Project"
