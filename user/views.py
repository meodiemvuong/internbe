from django.shortcuts import render
from rest_framework.views import Response, APIView
from rest_framework import permissions, exceptions
from django.contrib.auth import login, logout
from django.contrib.auth.models import AnonymousUser
from company.models import Company, Employee, Level
from user.models import User
from user.serializers import UserSerializer
# Create your views here.

class UserList(APIView):
    
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        return Response(serializer.data)
class UserLogin(APIView):
    def post(self, req):
        username = req.data.get('username')
        password = req.data.get('password')
        if not username or not password:
            raise exceptions.APIException({
                "message": "Don't find username"
            })
        user = User.objects.get(username = username)
        serializer = UserSerializer(user)
        if not (user.check_password(password)):
            raise exceptions.APIException({
                "message": "Incorrect Password"
            })
        login(user=user, request=req)
        return Response(serializer.data)
class UserLogout(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def post(self, req):
        logout(req)
        return Response({
            "message": "Logout success"
        })

class GetMe(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def get(self, req):
        user = User.objects.get(id=req.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UpdateCompany(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def get(self, req):
        user = User.objects.get(id=req.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, req):
        company = req.data.get('company')
        if company is None:
            raise exceptions.APIException({
                "message": "Don't have company field"
            })
        user = User.objects.get(id=req.user.id)
        try:
            getCompany = Company.objects.get(pk=company)
        except Company.DoesNotExist:
            raise exceptions.APIException({
                "message": "Don't find Company"
            })
        serializer = UserSerializer(user, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "message": "Have problem"
        })

class UpdateLevel(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def get(self, req):
        user = User.objects.get(id=req.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, req):
        level = req.data.get('level')
        if level is None:
            raise exceptions.APIException({
                "message": "Don't have level field"
            })
        user = User.objects.get(id=req.user.id)
        userSerializer = UserSerializer(user)
        if userSerializer.data['company'] is None:
            raise exceptions.APIException({
                "message": "You need join Company"
            }) 
        
        try:
            getLevel = Level.objects.get(pk=level)
        except Level.DoesNotExist:
            raise exceptions.APIException({
                "message": "Don't find level"
            })
        print(getLevel.get_company())
        if getLevel.get_company() != user.get_company():
            raise exceptions.APIException({
                "message": "Company don't have Level"
            })
        serializer = UserSerializer(user, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "message": "Have problem"
        })

class UpdateEmployee(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def get(self, req):
        user = User.objects.get(id=req.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, req):
        employee = req.data.get('employee')
        if employee is None:
            raise exceptions.APIException({
                "message": "Don't have employee field"
            })
        user = User.objects.get(id=req.user.id)
        userSerializer = UserSerializer(user)
        if userSerializer.data['company'] is None:
            raise exceptions.APIException({
                "message": "You need join Company"
            }) 
        
        try:
            getEmployee = Employee.objects.get(pk=employee)
        except Employee.DoesNotExist:
            raise exceptions.APIException({
                "message": "Don't find Employee"
            })
        if getEmployee.get_company() != user.get_company():
            raise exceptions.APIException({
                "message": "Company don't have Employee"
            })
        serializer = UserSerializer(user, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "message": "Have problem"
        })
