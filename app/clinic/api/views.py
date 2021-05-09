from django.shortcuts import get_object_or_404
from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from .serializers import ClinicSerializer,StaffSerializer
from clinic.models import Clinic,Staff




class ClinicView(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

    def list_clinic_staffs(self, request, pk):
        serializer_class= StaffSerializer
        print(pk)
        clinic = get_object_or_404(Clinic, id=pk)
        staffs = Staff.objects.filter(clinic_id=clinic.id)
        print(staffs)
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


