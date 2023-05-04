from django.contrib import admin

from .models import Message

#регистрация в админке
admin.site.register(Message)
