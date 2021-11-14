from teacher.models import Teacher
from rest_framework import serializers

class CreateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'years_of_experience']

class UpdateTeacherSerializer(serializers.ModelSerializer, serializers.Serializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'years_of_experience']
        extra_kwargs = {'username': {'read_only': True}, 'password': {'read_only': True}}
    
    years_of_experience = serializers.CharField(max_length=100, required=False)