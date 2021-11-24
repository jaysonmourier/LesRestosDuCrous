from django import forms

class CategorieForm(forms.Form):
    nom = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    #image = forms.ImageField(widget=forms.TextInput(attrs={'class':'custom-file-input', 'type': 'file', 'name': 'image', 'accept': 'image/*', 'required': True, 'id': 'id_image'}))
    #unite = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'number', 'name': 'unite', 'required': True, 'id': 'id_unite'}))