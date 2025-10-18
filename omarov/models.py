from config.models import BaseModel
from django.db import models
from django_resized import ResizedImageField
from django.utils import timezone
from django.core.exceptions import ValidationError

class Photo(BaseModel):
    author = models.CharField(max_length=20, default="Unknown")
    image = ResizedImageField(size = [450,600], force_format = "WEBP", upload_to="photos/", quality=100,)
    date = models.DateTimeField(auto_now_add=True)
    
    # def clean(self): # FIXME
    #     if self.date.date() > timezone.now().date():
    #         raise ValidationError("The date of the photo cannot be in the future.")