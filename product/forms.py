from django.db.models.base import Model
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nom", "categorie", "uniteStock"]

class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nom", "uniteStock", "threshold"]