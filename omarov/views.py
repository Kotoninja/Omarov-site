from django.shortcuts import render


def biography(request):
    return render(request, "omarov/biography.html")

def gallery(request):
    return render(request,"omarov/gallery.html")