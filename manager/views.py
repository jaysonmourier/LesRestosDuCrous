from django.shortcuts import redirect, render

def index(request) -> render:
    if not request.user.is_authenticated:
        return redirect("/manager/login")
    return render(request, "manager/index.html")

def login(request) -> render:
    if request.user.is_authenticated:
        return redirect("/manager/")
    return render(request, "manager/login.html")