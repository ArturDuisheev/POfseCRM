import django_filters
from django_filters import rest_framework as filters

from .models import Client


class ClientFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ('keyword',)


class ClientFilter(filters.FilterSet):
    keyword = filters.CharFilter(field_name='name_organization', lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['keyword']

        ordering = ['name_organization']

        def custom_search(self, queryset, name, value):
            return queryset.filter(name_organization__icontains=value)
