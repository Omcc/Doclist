from rest_framework import permissions
from clinic.models import Staff,Clinic
from django.core.exceptions import ObjectDoesNotExist
class isClinicOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class isStaffOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(request.user)
        return obj.clinic.user == request.user

    def has_permission(self,request,view):

        print(request.data)

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE':
            return True
        if not request.data:
            return False

        clinic_id = request.data['clinic']

        if clinic_id is not None:
            try:
                clinic = Clinic.objects.get(pk=clinic_id)
            except ObjectDoesNotExist:
                return False
            return clinic.user == request.user

        return False












class isStaffImageOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.staff.clinic.user == request.user

    def has_permission(self,request,view):


        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.data:
            return False

        staff_id = request.data['staff']

        if staff_id is not None:
            try:
                staff = Staff.objects.get(pk=staff_id)
            except ObjectDoesNotExist:
                return False
            return staff.clinic.user == request.user
        return False
