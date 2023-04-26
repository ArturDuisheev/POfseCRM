from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import EmployeeRegisterSerializer
from .models import EmployeeRegister


class EmployeeRegisterAPIView(CreateAPIView):
    queryset = EmployeeRegister.objects.all()
    serializer_class = EmployeeRegisterSerializer

