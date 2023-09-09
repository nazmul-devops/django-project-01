from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from dbpost.views.post_list_view import *
from . import views

app_name = "dbpost"

urlpatterns = ([
    path('', api_home_page, name='api_home_page'),
    path("posts/", post_list, name='post_list'),
    path("post-details/<int:post_id>", post_details_view, name='post_details_view'),
    path("post-create/", post_create_form_view, name='post_create_form_view'),
])