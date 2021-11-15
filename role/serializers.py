from rest_framework import serializers
from .models import Role

class CreateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('user', 'role')

class UpdateRoleSerializer(serializers.ModelSerializer, serializers.Serializer):
    class Meta:
        model = Role
        fields = ('user', 'role')