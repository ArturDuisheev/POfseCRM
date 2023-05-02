import django_filters

from .models import Client


class ClientFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ('keyword',)


"""Доработать filters(Artur)"""


# field_names = 'name_client', 'name_organization'.join(" ")

# class ClientFilter(filters.FilterSet):
#     name_organization = filters.CharFilter(field_name='name_organization')
#     name_client = filters.CharFilter(field_name='name_client')
#     keyword = filters.CharFilter(field_name=field_names, method='custom_filter', lookup_expr='icontains')
#
#     class Meta:
#         model = Client
#         fields = ['name_organization', 'name_client']
#         filterset_method = 'custom_filter'
#
#     def custom_filter(self, queryset, name, value):
#         return queryset.filter(
#             Q(name_organization__icontains=value) |
#             Q(name_client__icontains=value)
#         )
