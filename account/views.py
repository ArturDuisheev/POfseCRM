# from django.contrib.auth import authenticate
# from rest_framework import permissions, generics
# from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
#
# from .serializers import UserRegisterSerializer
# from .models import User
#
#
# class RegisterUserAPIView(CreateAPIView):
#     """
#     Регистрация пользователя
#     """
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer
#     permission_classes = (permissions.IsAdminUser,)
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = UserRegisterSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "Регистрация прошла успешно!",
#                 "data": serializer.data
#             }
#             return Response(data=response)
#         else:
#             data = serializer.errors
#             return Response({"message": "Что-то пошло не так!",
#                              "data": data})
