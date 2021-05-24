from rest_framework import serializers

from administration.models import Address,Country,City,District,County,Language,Specialization,Title,Job

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"







class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = "__all__"
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields ="__all__"

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields ="__all__"

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
