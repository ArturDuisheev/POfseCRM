from rest_framework import serializers
from .models import Project, Client


class ProjectSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(read_only=True, format="%d.%m.%Y")
    date_updated = serializers.DateTimeField(read_only=True, format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = Project
        fields = 'name_project description status currency amount stars date_created date_updated'.split()


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name_organization', 'name_client', 'project', 'address', 'city', 'country', 'phone', 'email',
                  'status')
        read_only_fields = ('id',)
