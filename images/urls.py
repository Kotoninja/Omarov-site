from django.urls import path
from images import views

app_name = "images"

urlpatterns = [
    path("add/", views.add, name="add")
]
