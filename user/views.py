from django.shortcuts import render

def show(request) -> render:
    pass

def register(request) -> render:
    return render(request, "user/register.html")