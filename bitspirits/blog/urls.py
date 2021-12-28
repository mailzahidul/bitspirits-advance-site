from django.conf.urls import url

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name="blogs"),
    path('details/<id>', views.blog, name="blog"),
]
