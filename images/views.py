from django.shortcuts import render, redirect
from django.urls import reverse
from images.forms import AddPhoto

def add(request):
    if request.method == "POST":
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("omarov:gallery"))
 
    return redirect(reverse("omarov:gallery"))