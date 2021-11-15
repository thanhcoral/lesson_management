from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrTeacherOfCourse(BasePermission):
    def has_permission(self, request, obj):
        return bool(request.user.role.role == 'Teacher' or request.user.is_staff)

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.role.role == 'Student')