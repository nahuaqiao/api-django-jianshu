from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj)
        print(obj.user.id)
        print(request.user)
        return obj.user.id == request.user.id
