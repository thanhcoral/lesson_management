from .models import Student
from role.models import Role
from .serializer import CreateStudentSerializer, UpdateStudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser
# Create your views here.
class StudentList(APIView):
    
    permission_classes = (IsAdminUser, )
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = CreateStudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateStudentSerializer(data=request.data)
        if serializer.is_valid():
            password = make_password(self.request.data['password'])
            student = serializer.save(password=password)
            role = Role(user=student, role='Student') 
            role.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        if not (self.request.user.id == student.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        serializer = UpdateStudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        if not (self.request.user.id == student.id or self.request.user.is_staff):
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        serializer = UpdateStudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        if not self.request.user.is_staff:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)