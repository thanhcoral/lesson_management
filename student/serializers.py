from rest_framework import serializers
from student.models import Student

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address']

class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address']
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}
    
    address = serializers.CharField(max_length=20, required=False)