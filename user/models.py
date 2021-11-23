from django.db import models

class Beneficiaire(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=10)
    adresse = models.CharField(max_length=30)
    NBPARTS_CHOICES = [
        ('0', '0-3'),
        ('1', '4-14'),
        ('2', '15-25'),
        ('3', '25-64'),
        ('4', 'Plus de 65'),
    ]
    nbParts = models.CharField(max_length=10, choices=NBPARTS_CHOICES, default='2')
    motMairie = models.BooleanField()
    carteDonnee = models.BooleanField()
    presenceDistribution = models.BooleanField()
    remarque = models.CharField(max_length=255)
    validated = models.BooleanField(default=0)