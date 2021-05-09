from django.shortcuts import get_object_or_404
from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from .serializers import ClinicSerializer,StaffSerializer
from clinic.models import Clinic,Staff




class ClinicView(viewsets.ModelViewSet):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

    def get_queryset(self):
        return Staff.objects.filter(clinic=self.kwargs['clinic_pk'])


