from django.shortcuts import get_object_or_404
from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from .serializers import ClinicSerializer
from clinic.models import Clinic


class ClinicView(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
