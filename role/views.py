from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateRoleSerializer, UpdateRoleSerializer
from .models import Role
from django.http import Http404
from rest_framework.permissions import IsAdminUser
# Create your views here.

class RoleList(APIView):
    """
    Just admin can get role list and create a new role
    """
    permission_classes = (IsAdminUser, )
    def get(self, request, format=None):
        courses = Role.objects.all()
        serializer = CreateRoleSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleDetail(APIView):
    """
    Just admin has permission to get, update and delete a role
    """
    permission_classes = (IsAdminUser, )
    def get_object(self, pk):
        try:
            return Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = UpdateRoleSerializer(role)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = UpdateRoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)