from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= User
        fields= ('id','email','first_name','last_name','password','name')

        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 4},
            'first_name':{'write_only':True},
            'last_name':{'write_only':True}
        }

    def get_name(self,obj):
        name = obj.first_name
        if name=='':
            name = obj.email
        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= User
        fields= ['id','email','name','token']

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token["test"] = "test"
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k]=v

        return data

