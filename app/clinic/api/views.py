from django.shortcuts import get_object_or_404
from rest_framework import generics, status,viewsets,mixins
from rest_framework.response import Response
from .serializers import ClinicSerializer,StaffSerializer,ClinicImageSerializer,StaffImageSerializer,ClinicTypeSerializer
from clinic.models import Clinic,Staff,ImageClinic,ImageStaff,ClinicType
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import isClinicOwnerOrReadOnly,isStaffOwnerOrReadOnly,isStaffImageOwnerOrReadOnly
from administration.models import Language,Specialization,Title
from django.db import transaction


class ClinicTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClinicType.objects.all()
    serializer_class = ClinicTypeSerializer

class ClinicView(viewsets.ModelViewSet):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class StaffView(viewsets.ModelViewSet):

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

    def get_queryset(self):
        return Staff.objects.filter(clinic=self.kwargs['clinic_pk'])

    @transaction.atomic
    def update(self,request,*args,**kwargs):

        data = request.data
        staff = self.get_object()
        staff.languages.clear()
        staff.specialisations.clear()

        languages = data.pop("languages")
        print(languages)
        specialisations = data.pop("specialisations")


        for language_id in languages:
            try:
                language = Language.objects.get(pk=language_id)
                staff.languages.add(language)
            except KeyError:
                pass
        for spec_id in specialisations:
            try:
                specialisation = Specialization.objects.get(pk=spec_id)
                staff.specialisations.add(specialisation)
            except KeyError:
                return Response(KeyError)

        serializer = self.get_serializer(staff,data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class ClinicImageView(viewsets.ModelViewSet):
    serializer_class = ClinicImageSerializer
    queryset = ImageClinic.objects.all()

    def get_queryset(self):
        return ImageClinic.objects.filter(clinic=self.kwargs['clinic_pk'])




class StaffImageView(viewsets.ModelViewSet):
    permission_classes = [isStaffImageOwnerOrReadOnly]
    serializer_class = StaffImageSerializer
    queryset = ImageStaff.objects.all()

    def get_queryset(self):
        return ImageStaff.objects.filter(staff=self.kwargs['staff_pk'])