from django.shortcuts import render        

# Index view
def index(request) -> render:
    return render(request, "index.html")