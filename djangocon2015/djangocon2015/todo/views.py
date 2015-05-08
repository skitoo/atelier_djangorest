
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from . import serializers, models


class Category(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category


class Task(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.Task

    @list_route()
    def mine(self, request):
        queryset = self.filter_queryset(
            self.get_queryset().filter(owner=request.user)
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
