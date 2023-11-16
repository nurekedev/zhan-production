from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    
# class IsStaffEditorPermission(permissions.DjangoModelPermissions):
#     def has_permission(self, request, view):
#         if request.user.is_staff:
#             return True
#         return False