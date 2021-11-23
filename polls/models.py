from django.db import models
from django.http.request import MediaType

class Beneficiaire(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    NBPARTS_CHOICES = [
        ('0', '0-3'),
        ('1', '4-14'),
        ('2', '15-25'),
        ('3', '25-64'),
        ('4', 'Plus de 65'),
    ]
    NbParts = models.CharField(max_length=10, choices=NBPARTS_CHOICES, default='2')
    MotMairie = models.BooleanField()
    CarteDonnee = models.BooleanField()
    PresenceDistribution = models.BooleanField()
    Remarque = models.CharField(max_length=255)