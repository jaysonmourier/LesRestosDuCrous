from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.show_unconfirmed, name='show_unconfirmed'),
    path('<int:page>', views.show_unconfirmed, name='show_unconfirmed'),
    path('register/', views.register, name='register')
]