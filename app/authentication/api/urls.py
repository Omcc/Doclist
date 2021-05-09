from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from . import views


urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/profile/',views.getUserProfile,name="users-profile"),
    path('clinic/register/',views.createClinic,name="create-clinic")
]