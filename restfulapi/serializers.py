from rest_framework import serializers
from restfulapi import models
from django.contrib.auth import get_user_model
from django.contrib import auth
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.certification
        fields = ('id', 'name')
        read_only_fields = ('id',)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ( 'username','password','first_name','last_name')

    def validate(self, attrs):
        user = auth.authenticate(username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def list(self):
        return get_user_model().objects.all()
    
    def getByname(self,name):
        return get_user_model().objects.get(username=name)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.message
        fields = ('id', 'message','user','time')
        read_only_fields = ('id',)
