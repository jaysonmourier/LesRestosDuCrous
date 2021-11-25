from django.forms import ModelForm

from .models import Beneficiaire

class UserForm(ModelForm):
    class Meta:
        model = Beneficiaire
        fields = ["prenom", "nom", "email", "telephone", "adresse", "nbParts", "motMairie", "carteDonnee", "presenceDistribution", "remarque"]

#class UserForm(forms.Form):
#    first_name = forms.CharField(label='Prénom', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
#    last_name = forms.CharField(label='Nom de famille', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
#    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
#    telephone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    #adresse = forms.CharField(max_length=30)
    #nbParts = forms.CharField(max_length=10)
    #motMairie = forms.BooleanField()
    #carteDonnee = forms.BooleanField()
    #presenceDistribution = forms.BooleanField()
    #remarque = forms.CharField(max_length=255)
    #validated = forms.BooleanField()