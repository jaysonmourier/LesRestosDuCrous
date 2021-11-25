from django.forms import ModelForm

from .models import Beneficiaire

class UserForm(ModelForm):
    class Meta:
        model = Beneficiaire
        fields = ["prenom", "nom", "email", "telephone", "adresse", "nbParts", "motMairie", "carteDonnee", "presenceDistribution", "remarque"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['remarque'].required = False