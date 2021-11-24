from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CategorieForm
from .models import Categorie

@login_required(redirect_field_name=None)
def index(request) -> render:

    if request.method == "POST":
        categorieForm = CategorieForm(request.POST)
        if categorieForm.is_valid():
            categorie = Categorie()
            categorie.nom = categorieForm.cleaned_data['nom']
            # default value
            categorie.image = "/static/default.jpeg"
            categorie.unite = 0
            categorie.save()
        else:
            print("[LOG] invalid form!")
    else:
        categorieForm = CategorieForm()
    
    all_entries = Categorie.objects.all()
    print(all_entries.values("nom"))

    return render(request, "categorie/index.html", {"form": categorieForm, "categories": all_entries})