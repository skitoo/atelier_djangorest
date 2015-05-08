from django.conf import settings
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    categories = models.ManyToManyField(Category, related_name='tasks')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
