from django.db import models
from django import forms

class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)