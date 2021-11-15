from .models import Lesson
from rest_framework import serializers

class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'time', 'teacher', 'students']

class UpdateLessonSerializer(serializers.ModelSerializer, serializers.Serializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'time', 'teacher', 'students']
        extra_kwargs = {
            'teacher': {'read_only': True}, 
            'students': {'read_only': True}
            }
    name = serializers.CharField(max_length=200, required=False)
    time = serializers.CharField(max_length=200, required=False)
        