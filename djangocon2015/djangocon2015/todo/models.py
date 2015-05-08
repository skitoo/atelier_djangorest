from django.db import models
from django.conf import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ManyToManyField(Category, related_name='tasks')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
