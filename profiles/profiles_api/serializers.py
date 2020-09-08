from rest_framework import serializers
from rest_framework.serializers import Serializer


class HelloSerializer(Serializer):
    name = serializers.CharField(max_length=10)
    