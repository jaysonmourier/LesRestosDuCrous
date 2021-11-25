from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import UserForm
from .models import Beneficiaire

@login_required(redirect_field_name=None)
def show_unconfirmed(request, page):
    beneficiaires = Beneficiaire.objects.all().filter(validated=0)
    paginator = Paginator(beneficiaires, 5)
    beneficiaires_obj = paginator.get_page(page)
    return render(request, "user/show_unconfirmed.html", {"beneficiaire_obj": beneficiaires_obj})

def register(request):
    info_message = None
    info_type = None
    # Post query processing
    if request.method == "POST":
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            beneficiaire = Beneficiaire()
            beneficiaire.prenom = userForm.cleaned_data['prenom']
            beneficiaire.nom = userForm.cleaned_data['nom']
            beneficiaire.email = userForm.cleaned_data['email']
            beneficiaire.telephone = userForm.cleaned_data['telephone']
            beneficiaire.adresse = userForm.cleaned_data['adresse']
            beneficiaire.nbParts = userForm.cleaned_data['nbParts']
            beneficiaire.motMairie = userForm.cleaned_data['motMairie']
            beneficiaire.carteDonnee = userForm.cleaned_data['carteDonnee']
            beneficiaire.presenceDistribution = userForm.cleaned_data['presenceDistribution']
            beneficiaire.remarque = userForm.cleaned_data['remarque']
            
            if request.user.is_authenticated:
                beneficiaire.validated = True
            else:
                beneficiaire.validated = False

            beneficiaire.save()

            info_message = "Votre demande a été prise en compte."
            info_type = "success"
        else:
            info_message = "La demande ne peut être faite. Assurez-vous qu'une demande avec la même adresse email n'est pas déjà en cours."
            info_type = "danger"
    else:
        userForm = UserForm()
    
    return render(request, "user/register.html", {'form': userForm, 'message': info_message, 'type': info_type})