
from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models


class Category(serializers.ModelSerializer):
    class Meta:
        model = models.Category


class Task(serializers.ModelSerializer):

    owner = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all()
    )

    categories = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Category.objects.all(),
        many=True
    )

    class Meta:
        model = models.Task
        fields = ('id', 'name', 'owner', 'categories', 'done')
