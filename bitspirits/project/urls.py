from django.conf.urls import url

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.Projects, name="projects"),
    path('details/<id>', views.details, name="project"),
]
