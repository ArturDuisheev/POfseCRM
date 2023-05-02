import django_filters
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from .filters import ClientFilter


class CreateUpdateViewSetMixin:
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        responce = {
            "status": "Клиент успешно создан",
            # "data": serializer.data
        }
        headers = self.get_success_headers(serializer.data)
        return Response(responce, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        responce = {
            "status": "Клиент успешно обновлен",
            # "data": serializer.data
        }
        headers = self.get_success_headers(serializer.data)
        return Response(responce, status=status.HTTP_200_OK, headers=headers)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        responce = {
            "status": "Клиент успешно удален"
        }
        headers = self.get_success_headers(responce)
        return Response(responce, status=status.HTTP_204_NO_CONTENT, headers=headers)


class ProjectViewSet(CreateUpdateViewSetMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        responce = {
            "status": "Проект успешно создан",
            # "data": serializer.data
        }
        headers = self.get_success_headers(serializer.data)
        return Response(responce, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        responce = {
            "status": "Проект успешно обновлен",
            # "data": serializer.data
        }
        headers = self.get_success_headers(serializer.data)
        return Response(responce, status=status.HTTP_200_OK, headers=headers)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        responce = {
            "status": "Проект успешно удален"
        }
        headers = self.get_success_headers(responce)
        return Response(responce, status=status.HTTP_204_NO_CONTENT, headers=headers)

    def perform_destroy(self, instance):
        super(ProjectViewSet, self).perform_destroy(instance)
        Project.objects.filter(id__gt=instance.id).update(id=F('id') - 1)


class ClientViewSet(CreateUpdateViewSetMixin, ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ClientFilter
