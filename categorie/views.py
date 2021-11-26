from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.paginator import Paginator

from .forms import CategorieForm, UpdateCategorie
from .models import Categorie

def _getCategorieOrRedirect(id):
    try:
        categorie = Categorie.objects.get(id=id)
    except:
        return None
    return categorie

@login_required(redirect_field_name=None)
def delete(request, id):
    Categorie.objects.all().filter(id=id).delete()
    return redirect(f"/categorie/")

@login_required(redirect_field_name=None)
def index(request, page=1):
    # POST query processing
    if request.method == "POST":
        categorieForm = CategorieForm(request.POST)
        if categorieForm.is_valid():
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
        categorieForm = CategorieForm()

    # pagination
    all_entries = Categorie.objects.all().filter().order_by('-id')    
    paginator = Paginator(all_entries, 5)
    page_obj = paginator.get_page(page)

    return render(request, "categorie/index.html", {"form": categorieForm, "page_obj": page_obj, "count": paginator.count})

@login_required(redirect_field_name=None)
def update(request, id):
    if request.method == "POST":
        categorie = _getCategorieOrRedirect(id)
        if categorie == None: return redirect("/categorie/")
        categorieForm = UpdateCategorie(request.POST, instance=categorie)
        if categorieForm.is_valid():
            categorie.nom = categorieForm.cleaned_data['nom']
            categorie.save()
            return redirect("/categorie/")

    else:
        categorie = _getCategorieOrRedirect(id)
        if categorie == None: return redirect("/categorie/")
        productForm = UpdateCategorie(instance=categorie)

    return render(request, "categorie/update.html", {"form": productForm, "id": id})