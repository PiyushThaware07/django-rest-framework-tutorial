from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ["username","email","password","password_confirmation"]
        extra_kwargs = {
            "password" : {"write_only":True}
        }
    def save(self):
        password = self.validated_data['password']
        confirm_password = self.validated_data['password_confirmation']
        if password != confirm_password:
            raise serializers.ValidationError({'error':'password is not same'})
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'error','Emil already exists!'})
        account = User(email=self.validated_data['email'],username = self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account