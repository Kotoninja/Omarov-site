from django.urls import path
from images import views

app_name = "images"

urlpatterns = [
    path("add/", views.add, name="add"),
    path("<slug>", views.image_preview, name="image_preview")
]
