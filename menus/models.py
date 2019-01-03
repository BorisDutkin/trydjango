from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from restaurants.models import RestaurantLocation


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='separate each item by comma')
    excludes = models.TextField(blank=True, null=True, help_text='separate each item by comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', 'timestamp']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    def get_contents(self):
        return self.contents.strip().split(",")

    def get_excludes(self):
        return self.excludes.strip().split(",")
