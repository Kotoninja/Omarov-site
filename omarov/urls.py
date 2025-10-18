from django.urls import path

from . import views

app_name = "omarov"

urlpatterns = [
    path("omarov/", views.biography, name="biography"),
    path("gallery/", views.gallery, name="gallery"),
]
