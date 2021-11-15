import lesson
from .models import Lesson
from .serializer import CreateLessonSerializer, UpdateLessonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAdminUser, AllowAny
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
class LessonList(APIView):

    permission_classes = (IsAdminUser, )
    def get(self, request, format=None):
        lessons = Lesson.objects.all()
        serializer = CreateLessonSerializer(lessons, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CreateLessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonDetail(APIView):
    def get_object(self, pk):
        try:
            return Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lesson = self.get_object(pk)
        print(not (self.request.user.id == Lesson.teacher.id or request.user.is_staff))
        if self.request.user.id == lesson.teacher.id or request.user.is_staff:
            serializer = UpdateLessonSerializer(lesson)
            return Response(serializer.data)
        else:
            try:
                Lesson.students.get(id=self.request.user.id)
                serializer = UpdateLessonSerializer(Lesson)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk, format=None):
        lesson = self.get_object(pk)

        if not (self.request.user.id == lesson.teacher.id or request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        serializer = UpdateLessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if not self.request.user.is_staff:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        lesson = self.get_object(pk)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)