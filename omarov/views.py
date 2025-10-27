from django.shortcuts import render
from django.shortcuts import get_object_or_404
from images.models import Image
from images.forms import AddPhoto

def biography(request):
    return render(request, "omarov/biography.html")


def gallery(request):
    return render(
        request, "omarov/gallery.html", context={"photos": Image.objects.all(), "form": AddPhoto()}
    )
