from config.models import BaseModel
from django.db import models
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os

class Image(BaseModel):
    author = models.CharField(max_length=20, default="Unknown")
    image = ResizedImageField(
        size=[450, 600], force_format="WEBP", upload_to="photos/", quality=100
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.title:
            self.title = f"Photo №{self.pk}"
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Image, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Image)
def delete_img_pre_delete_post(sender, instance, *args, **kwargs):
    if instance.image:
        os.remove(instance.image.path)