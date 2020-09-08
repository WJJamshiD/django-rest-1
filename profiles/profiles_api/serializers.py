from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from profiles_api.models import UserProfile


class HelloSerializer(Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
    
        return user