from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.show_all_unconfirmed, name='show_all_unconfirmed'),
    path('<int:page>', views.show_all_unconfirmed, name='show_all_unconfirmed'),
    path('all', views.show_all_confirmed, name='show_all_confirmed'),
    path('all/<int:page>', views.show_all_confirmed, name='show_all_confirmed'),
    path('profil/<int:id>', views.show_unique_user, name='show_unconfirmed'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('confirm/<int:id>', views.confirm, name='confirm'),
    path('register/', views.register, name='register')
]