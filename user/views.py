from django.shortcuts import redirect, render

from .forms import UserForm

def show(request) -> render:
    pass

def register(request) -> render:
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = UserForm()
    return render(request, "user/register.html", {'form': form})