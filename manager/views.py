from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm 

@login_required(redirect_field_name=None)
def index(request) -> render:
    return render(request, "manager/index.html")

def loginPage(request) -> render:

    error_login = None

    if request.user.is_authenticated:
        return redirect("/manager/")
    
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = authenticate(
                request,
                username=loginForm.cleaned_data['username'], 
                password=loginForm.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect("/manager/login/")
            else:
                error_login = "Impossible de se connecter !"
    else:
        loginForm = LoginForm()

    return render(request, "manager/login.html", {'form': loginForm, 'error_login': error_login})

@login_required(redirect_field_name=None)
def logoutPage(request) -> render:
    logout(request)
    return redirect("/")