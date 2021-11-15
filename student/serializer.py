from .models import Student
from rest_framework import serializers

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address']

class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address']
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}
    
    address = serializers.CharField(max_length=200, required=False)