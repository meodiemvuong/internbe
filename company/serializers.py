from rest_framework import serializers

from company.models import Company, Level, Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields =['id', 'name', 'description']
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = ['name', 'age', 'company', 'id']
    
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['level', 'company', 'id']