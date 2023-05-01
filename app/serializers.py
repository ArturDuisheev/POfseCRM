from rest_framework import serializers
from .models import Project, Client


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name_organization', 'name_client', 'project', 'address', 'city', 'country', 'phone', 'email',
                  'status')
        read_only_fields = ('id', )
