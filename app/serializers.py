from rest_framework import serializers
from .models import Project, Client


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     response_data = {}
    #     for field in validated_data:
    #         old_value = getattr(instance, field)
    #         new_value = validated_data.get(field, old_value)
    #         if new_value != old_value:
    #             response_data[
    #                 f'изменено поле {field}'] = f'Старое значение: {old_value}, новое значение: {new_value}'
    #         setattr(instance, field, new_value)
    #     instance.save()
    #     response_data['message'] = 'Объект успешно обновлен'
    #     return response_data


# def set_project(obj):
#     return ProjectSerializer(obj.project, many=False).data
#
#
# def get_project(obj):
#     return ProjectSerializer(obj.project, many=True).data


class ClientSerializer(serializers.ModelSerializer):
    # date_created = serializers.DateTimeField(format="%d.%m.%Y добавленно: %S секунд назад")
    # date_updated = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = Client
        fields = 'id name_organization name_client project address city country phone email ' \
                 'status'.split()

        extra_kwargs = {
            'id': {'read_only': True},
        }

