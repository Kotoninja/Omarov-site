from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from images.forms import AddPhoto
from .models import Image
from django.http import HttpResponse

def add(request):
    if request.method == "POST":
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()
            response = render(request,"images/image_frame.html",{"photo":image})
            response["HX-Trigger"] = "add-photo-success"
            return response

def image_preview(request, slug):
    image = get_object_or_404(Image, slug=slug)
    return render(request,"omarov/image_preview.html", {"image":image})
