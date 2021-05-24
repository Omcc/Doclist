from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authentication.models import User
from clinic.models import Clinic,ClinicType,Staff,ImageClinic,ImageStaff
from rest_framework_simplejwt.tokens import RefreshToken
from administration.models import Address
from administration.api.serializers import AddressSerializer,LanguageSerializer,SpecializationSerializer,TitleSerializer,JobSerializer
from authentication.api.serializers import UserSerializer
from django.contrib.auth.hashers import make_password



class StaffImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageStaff
        fields = ["id","image","default","staff"]

class ClinicTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClinicType
        fields = ["id","name"]
        depth=1

class StaffSerializer(serializers.ModelSerializer):
    images = StaffImageSerializer(many=True,required=False)
    languages = LanguageSerializer(many=True,required=False)
    specialisations = SpecializationSerializer(many=True,required=False)



    class Meta:
        model = Staff
        fields = ("id", "firstname","lastname","telephone","gender","title","job","description","clinic","images","languages","specialisations","email")
        read_only_fields = ('images',)
        extra_kwargs = {"telephone": {"required": False, "allow_null": True},
                        "gender": {"required": False, "allow_null": True},
                        "specialisations": {"required": False, "allow_null": True},
                        "languages": {"required": False, "allow_null": True},
                        "job": {"required": False, "allow_null": True},
                        "title": {"required": False, "allow_null": True},

                        }
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['job'] = JobSerializer(instance.job).data
        ret['title'] = TitleSerializer(instance.title).data
        return ret




class ClinicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClinic
        fields = ["image","default","clinic"]





class ClinicSerializer(serializers.ModelSerializer):
    clinic_type = serializers.PrimaryKeyRelatedField(
        queryset= ClinicType.objects.all(),required=True
    )
    address = AddressSerializer(many=False)
    user = UserSerializer(many=False)
    images = ClinicImageSerializer(many=True,required=False)

    class Meta:
        model= Clinic
        fields = ["id","name","address","description","clinic_type","user","telephone","images"]
        read_only_fields=('clinic_type',"address")

    def create(self,validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data,is_active=False)
        address_data= validated_data.pop('address')
        address = Address.objects.create(**address_data)
        clinic = Clinic.objects.create(**validated_data,address=address,user=user)
        staff = Staff.objects.create(firstname=user_data["firstname"],
                                                  lastname=user_data["lastname"],
                                                  clinic_id = clinic.id)

        return clinic








