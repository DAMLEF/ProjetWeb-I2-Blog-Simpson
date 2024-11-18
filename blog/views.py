from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages

from .models import *
from .forms import MoveForm


# Create your views here.
def post_list(request):
    simpsons = Simpson.objects.filter().order_by('age')
    places = Place.objects.filter().order_by('id_place')
    return render(request, 'blog/post_list.html', {'simpsons': simpsons, 'places': places})


def character_detail(request, id_character):
    simpson = get_object_or_404(Simpson, id_character=id_character)
    place = simpson.lieu
    if request.method == "POST":
        form = MoveForm(request.POST, instance=simpson)
        if form.is_valid():
            ancien_lieu = get_object_or_404(Place, id_place=place)
            ancien_lieu.disponibilite = "libre"
            ancien_lieu.save()

            form.save(commit=False)

            np = simpson.lieu.id_place
            nouveau_lieu = get_object_or_404(Place, id_place=np)

            if nouveau_lieu.disponibilite == "libre":
                if np != "Salon":    # Le Salon est la seule pièce qui peut accueillir plusieurs personnes !
                    nouveau_lieu.disponibilite = "occupé"
                    nouveau_lieu.save()

                if np == "Cuisine" and simpson.etat == "Affamé":
                    simpson.etat = "Content"
                elif np =="Jardin" and simpson.etat == "Stressé":
                    simpson.etat = "Content"
                elif np=="Sous-sol" and simpson.etat == "Curieux":
                    simpson.etat = "Content"
                elif np=="Sous-sol" and simpson.etat == "Stressé":
                    simpson.etat = "Affamé"

                simpson.save()
                return redirect('character_detail', id_character=id_character)
            else:
                messages.error(request, "⚠️ Le lieu est déjà occupé !")
                return redirect('character_detail', id_character=id_character)

    form = MoveForm()
    image_path = f"images/{simpson.surnom}_Simpson.png"
    return render(request, 'blog/character_detail.html', {'simpson': simpson, 'lieu': place, 'form': form, 'photo_path': image_path})
