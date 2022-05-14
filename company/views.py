from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from user.models import User
from rest_framework.views import Response, APIView
from company.models import Company, Level, Employee
from company.serializers import CompanySerializer, EmployeeSerializer, LevelSerializer
from user.serializers import UserSerializer
# Create your views here.
class CompanyViews(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyCreate(generics.ListCreateAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class GetUserCompany(APIView):
    def get(self, req, pk):
        user = User.objects.filter(company=pk)
        userSe = UserSerializer(user, many=True)
        return Response(userSe.data)
# Views Level

class LevelViews(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelCreate(generics.ListCreateAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelDetail(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class GetUserLevel(APIView):
    def get(self, req, pk):
        user = User.objects.filter(level=pk)
        userSe = UserSerializer(user, many=True)
        return Response(userSe.data)
# Views Employee

class EmployeeViews(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreate(generics.ListCreateAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class GetUserEmployee(APIView):
    def get(self, req, pk):
        user = User.objects.filter(employee=pk)
        userSe = UserSerializer(user, many=True)
        return Response(userSe.data)

