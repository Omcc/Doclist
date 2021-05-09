from django.urls import path,include

from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers





clinic_list = views.ClinicView.as_view({
    'get':'list',
    'post':'create'
})

clinic_detail = views.ClinicView.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

staff_list = views.StaffView.as_view({
    'get':'list',
    'post':'create',
})


router = routers.SimpleRouter()
router.register('clinics',views.ClinicView,basename='clinics')
staff_router = routers.NestedSimpleRouter(
    router,
    r'clinics',
    lookup='clinic'
)

staff_router.register(
    r'staffs',
    views.StaffView,
    basename="clinic-staff"
)

urlpatterns = [
    path('',include(router.urls)),
    path('',include(staff_router.urls))
]