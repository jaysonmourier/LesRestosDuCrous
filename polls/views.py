from django.shortcuts import redirect, render

# Index view
def index(request) -> render:
    # if you are logged in you are redirected to the manager's page
    if request.user.is_authenticated:
        return redirect('manager/')
    return render(request, "polls/home.html")