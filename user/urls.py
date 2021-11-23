from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('show/', views.show, name='show'),
    path('register/', views.register, name='register')
]