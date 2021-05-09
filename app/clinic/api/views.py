from django.shortcuts import get_object_or_404
from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from .serializers import ClinicSerializer,StaffSerializer,ClinicImageSerializer,StaffImageSerializer
from clinic.models import Clinic,Staff,ImageClinic,ImageStaff




class ClinicView(viewsets.ModelViewSet):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

    def get_queryset(self):
        return Staff.objects.filter(clinic=self.kwargs['clinic_pk'])

class ClinicImageView(viewsets.ModelViewSet):
    serializer_class = ClinicImageSerializer
    queryset = ImageClinic.objects.all()

    def get_queryset(self):
        return ImageClinic.objects.filter(clinic=self.kwargs['clinic_pk'])


class StaffImageView(viewsets.ModelViewSet):
    serializer_class = StaffImageSerializer
    queryset = ImageStaff.objects.all()

    def get_queryset(self):
        return ImageStaff.objects.filter(staff=self.kwargs['staff_pk'])