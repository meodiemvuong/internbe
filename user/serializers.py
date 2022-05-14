from user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'company', 'level', 'employee']
    def create(self, validate_data):
        password = validate_data.get('password')
        data = self.Meta.model(validate_data)
        if password is None and len(password)<6:
            return False
        data.set_password(password)
        data.save()
        return data
