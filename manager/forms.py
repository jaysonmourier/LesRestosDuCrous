from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'type': 'text', 'id': 'floatingInput', 'placeholder': 'username'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'id': 'floatingPassword', 'placeholder': 'Mot de passe'}))