from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('course_detail', views.course_detail, name="course_detail"),
    path('demo', views.demo, name="demo"),
]
