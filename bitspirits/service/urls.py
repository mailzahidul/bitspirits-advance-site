from django.conf.urls import url

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.Services, name="services"),
    path('details/<id>', views.ServiceDetails, name="details"),

]