from rest_framework import serializers

from .models import User, EmployeeRegister


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=16)
    position = serializers.ChoiceField(choices=[
        (1, 'Back-end Developer'),
        (2, 'Front-end Developer'),
        (3, 'UX/UI Designer'),
        (4, 'Marketing specialist'),
        (5, 'Sales manager'),
        (6, 'HR manager'),
        (7, 'Product manager'),
        (8, 'Project manager'),
        (9, 'CEO, founders'),
        (10, 'others')

    ], default=1)

    class Meta:
        model = EmployeeRegister
        fields = ['user', 'email', 'password', 'position']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
