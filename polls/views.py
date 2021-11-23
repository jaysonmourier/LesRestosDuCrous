from django.shortcuts import redirect, render

# Index view
def index(request) -> render:
    # if you are not logged in you are redirected to the home page
    if not request.user.is_authenticated:
        return render(request, "polls/not_authenticated.html")
    return render(request, "polls/index.html")

def login(request) -> render:
    # If you are already logged in you are redirected to the home page
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "polls/login/login.html")

def register(request) -> render:
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "polls/login/register.html")