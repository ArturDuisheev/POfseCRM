from rest_framework import serializers

from account.models import User, POSITION


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    position = serializers.ChoiceField(choices=POSITION)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = 'id email position is_active is_staff is_superuser password password2'.split()

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Данная электронная почта уже используется!')
        return email

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают!'})
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


