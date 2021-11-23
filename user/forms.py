from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='Prénom', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Nom de famille', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    telephone = forms.CharField(max_length=10)
    #adresse = forms.CharField(max_length=30)
    #nbParts = forms.CharField(max_length=10)
    #motMairie = forms.BooleanField()
    #carteDonnee = forms.BooleanField()
    #presenceDistribution = forms.BooleanField()
    #remarque = forms.CharField(max_length=255)
    #validated = forms.BooleanField()