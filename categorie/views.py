from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.forms import formset_factory

from .forms import CategorieForm
from .models import Categorie

@login_required(redirect_field_name=None)
def delete(request, id):
    Categorie.objects.all().filter(id=id).delete()
    return redirect("/categorie/")

@login_required(redirect_field_name=None)
def index(request) -> render:
    if request.method == "POST":
        categorieForm = CategorieForm(request.POST)
        formset = formset_factory(request.POST, request.FILES)
        if categorieForm.is_valid() and formset.is_valid():
            categorie = Categorie()
            categorie.nom = categorieForm.cleaned_data['nom']
            # default value
            categorie.image = "/static/img/default.jpg"
            categorie.unite = 0            
            try:
                categorie.save()
            except IntegrityError:
                redirect("/categorie/")

        else:
            print("[LOG] invalid form!")
    else:
        categorieForm = CategorieForm()
    
    all_entries = Categorie.objects.all().filter().order_by('-id')
    
    counter = all_entries.count()

    return render(request, "categorie/index.html", {"form": categorieForm, "count": counter, "entries": all_entries})