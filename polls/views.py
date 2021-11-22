from django.shortcuts import render

# Index view
def index(request) -> render:
    if not request.user.is_authenticated:
        return render(request, "polls/not_authenticated.html")
    return render(request, "polls/index.html")