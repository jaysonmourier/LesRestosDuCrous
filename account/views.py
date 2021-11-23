from django.shortcuts import render, redirect

def login(request) -> render:
    # If you are already logged in you are redirected to the home page
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "account/login.html")

def register(request) -> render:
    return render(request, "account/register.html")