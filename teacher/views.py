from .models import Teacher
from role.models import Role
from .serializer import CreateTeacherSerializer, UpdateTeacherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import make_password
# Create your views here.
class TeacherList(APIView):
    """
    Just admin has permission to get all teacher list and create new teacher
    """
    permission_classes = (IsAdminUser, )
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = CreateTeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateTeacherSerializer(data=request.data)
        if serializer.is_valid():
            password = make_password(self.request.data['password'])
            teacher = serializer.save(password=password)
            role = Role(user=teacher, role='Student') 
            role.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetail(APIView):
    """
    Teacher can get their own information and update it
    Admin has permission to get, update or delete a teacher
    """
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        if not (self.request.user.id == teacher.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        serializer = UpdateTeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        if not (self.request.user.id == teacher.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        serializer = UpdateTeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        if not self.request.user.is_staff:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)