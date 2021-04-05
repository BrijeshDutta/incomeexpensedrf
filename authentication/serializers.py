from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length = 68, min_length = 6, write_only=True)
    
    class Meta:
        model=User
        fields = ['email', 'username', 'password']
    
    
    def validate(self,  attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        
        if not username.isalnum():
            raise serializers.ValidationError('The username should be alphanumeric - from serializer')
        return attrs
    
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length = 555)
    
    class Meta:
        model = User
        fields = ['token']
        

class LoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length = 68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)

    
    class Meta:
        model = User
        fields = ['email', 'password', 'username','tokens']
    
    def validate(self, attrs):
        
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        

        
        " authenticate user "
        
        user = auth.authenticate(email=email, password=password)
        
        print(user.password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }
            
        return super().validate(attrs)

class RequestPasswordResetEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=2)
    
    class Meta:
        fields = ['email']
    
    
    def validate(self, attrs):
        try:
            email = attrs.get('email','')
        
        except expression as identifier:
            pass
            
        
        return super().validate(attrs)
    