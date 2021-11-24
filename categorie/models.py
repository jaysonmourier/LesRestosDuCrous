from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField

class Categorie(models.Model):
    nom = CharField(max_length=30, unique=True)
    image = ImageField(upload_to='upload')
    unite = IntegerField()

    def __str__(self):
        return self.nom