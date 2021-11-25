from django.db import models
from categorie.models import Categorie

class Product(models.Model):
    nom = models.CharField(max_length=30)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload")
    uniteStock = models.IntegerField()
    threshold = models.IntegerField()