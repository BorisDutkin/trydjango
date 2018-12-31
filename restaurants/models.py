from django.utils.text import slugify
from django.db import models
from django.db.models.signals import pre_save
from .validators import validate_category
from django.contrib.auth.models import User


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def restaurant_location_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(restaurant_location_pre_save_receiver, sender=RestaurantLocation)

