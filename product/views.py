from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Product
from categorie.models import Categorie
from .forms import ProductForm

@login_required(redirect_field_name=None)
def index(request, page=1):
    # Post query processing
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        
        if productForm.is_valid():
            product = Product()
            product.nom = productForm.cleaned_data['nom']
            product.categorie = productForm.cleaned_data['categorie']
            product.image = "/static/img/default.jpg"
            product.uniteStock = productForm.cleaned_data['uniteStock']
            product.threshold = 5
            product.save()

            # Update categorie unite
            categorie = Categorie.objects.get(nom=productForm.cleaned_data['categorie'])
            categorie.unite = categorie.unite + 1
            categorie.save()

    else:
        productForm = ProductForm()

    # Pagination
    all_products = Product.objects.all().filter().order_by("-id")
    paginator = Paginator(all_products, 5)
    page_obj = paginator.get_page(page)

    return render(request, "product/index.html", {"products_obj": page_obj, "form": productForm, "count": paginator.count})

@login_required(redirect_field_name=None)
def delete(request, id):
    product = Product.objects.all().filter(id=id)
    categorie_id = product.values('categorie_id')[0]['categorie_id']
    # Update categorie unite
    categorie = Categorie.objects.get(id=categorie_id)
    categorie.unite = categorie.unite - 1
    categorie.save()
    # delete product
    product.delete()
    return redirect(f"/product/")