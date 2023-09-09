from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from dbpost.views.post_list_view import *
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "dbpost"

urlpatterns = [
    path('', api_home_page, name='api_home_page'),
    path("posts/", post_list, name='post_list'),
    path("post-details/<int:post_id>", post_details_view, name='post_details_view'),
    path("post-create/", post_create_form_view, name='post_create_form_view'),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Django Blog Project API",
      default_version='v1.0.0',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += swagger_urlpatterns