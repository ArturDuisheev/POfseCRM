from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer


class CreateUpdateViewSetMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class ProjectViewSet(CreateUpdateViewSetMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ClientViewSet(CreateUpdateViewSetMixin, ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
