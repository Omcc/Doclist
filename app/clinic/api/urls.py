from django.urls import path,include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clinics',views.ClinicView,basename='clinics')

urlpatterns = [
    path('',include(router.urls))
]