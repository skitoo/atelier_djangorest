
from rest_framework import filters, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from . import filters as todo_filters
from . import models, serializers


class Category(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category

    @detail_route()
    def mine(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        category = self.get_object()
        category.my_tasks = category.tasks.filter(owner=request.user)
        serializer = serializers.MyCategory(category, context={'request': request})
        return Response(serializer.data)


class Task(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.Task
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = todo_filters.Task

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
