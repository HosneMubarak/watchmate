from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields =['username','email', 'password', 'password2',]
        extra_kwargs ={
            'password': {'write_only':True}
        }
    def save(self,):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise ValidationError({'error': 'Password and password2 not matched!'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise ValidationError({'error': 'email already exists!'})
        account = User.objects.create(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(self.validated_data['password'])
        account.save()
        