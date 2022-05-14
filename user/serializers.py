from user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'company', 'level', 'employee']
        extra_kwargs = {
            'company': {'required': False},
            'level': {'required': False},
            'employee': {'required': False},

        }
    def create(self, validate_data):
        password = validate_data.get('password')
        data = self.Meta.model(**validate_data)
        if password is None and len(password)<6:
            return False
        data.set_password(password)
        data.save()
        return data
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     send = send_mail('Create User', "Hello" + str(self.data['username']), 'thanhbinh16092k1@gmail.com', [self.data['email']]
    #     , fail_silently=False)
    #     instance.save()
    #     return instance