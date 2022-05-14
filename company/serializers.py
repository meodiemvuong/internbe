from rest_framework import serializers

from company.models import Company, Level, Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        field =['name', 'description']
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        field = ['name', 'age', 'company']
    
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        field = ['level', 'company']