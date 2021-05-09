from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer,UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from authentication.models import User

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createClinic(request):
    data = request.data
    print(data['password'])
    hashed_password = make_password(data['password'])

    user= User.objects.create(
        email = data['email'],
        password=hashed_password,
        is_active=True
    )

    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

