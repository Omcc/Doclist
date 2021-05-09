from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('addresses',views.AddressView,basename='addresses')

urlpatterns = [
    path('countries/',views.CountryListView.as_view(),name='countries'),
    path('countries/<int:id>/cities/',views.CityListView.as_view(),name='cities'),
    path('cities/<int:id>/counties/',views.CountyListView.as_view(),name="counties"),
    path('',include(router.urls))

]
