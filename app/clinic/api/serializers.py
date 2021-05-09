from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authentication.models import User
from clinic.models import Clinic,ClinicType,Staff
from rest_framework_simplejwt.tokens import RefreshToken
from administration.models import Address
from administration.api.serializers import AddressSerializer
from authentication.api.serializers import UserSerializer
from django.contrib.auth.hashers import make_password



class ClinicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicType
        fields = ["id","name"]
        depth=1

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("id", "first_name","last_name","telephone","gender","description","clinic")






class ClinicSerializer(serializers.ModelSerializer):
    clinic_type = serializers.PrimaryKeyRelatedField(
        queryset= ClinicType.objects.all(),required=True
    )
    address = AddressSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model= Clinic
        fields = ["id","name","address","description","clinic_type","user","telephone"]
        read_only_fields=('clinic_type',"address")

    def create(self,validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data,is_active=False)
        address_data= validated_data.pop('address')
        address = Address.objects.create(**address_data)
        clinic = Clinic.objects.create(**validated_data,address=address,user=user)
        staff = Staff.objects.create(first_name=user_data["first_name"],
                                                  last_name=user_data["last_name"],
                                                  clinic_id = clinic.id)

        return clinic








