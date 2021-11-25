from django.shortcuts import redirect, render

from .forms import UserForm

def show(request):
    pass

def register(request):
    userForm = UserForm()
    return render(request, "user/register.html", {'form': userForm})