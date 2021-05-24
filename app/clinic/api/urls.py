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
router.register('clinic-types',views.ClinicTypeViewSet,basename="clinic-types")

staff_router = routers.NestedSimpleRouter(
    router,
    r'clinics',
    lookup='clinic'
)

clinic_image_router = routers.NestedSimpleRouter(
    router,
    r'clinics',
    lookup = 'clinic'
)



staff_router.register(
    r'staffs',
    views.StaffView,
    basename="clinic-staff"
)

staff_image_router = routers.NestedSimpleRouter(
    staff_router,
    r'staffs',
    lookup='staff'
)

clinic_image_router.register(
    r'images',
    views.ClinicImageView,
    basename='clinic-image'
)
staff_image_router.register(
    r'images',
    views.StaffImageView,
    basename='staff-image'
)

urlpatterns = [
    path('',include(router.urls)),
    path('',include(staff_router.urls)),
    path('',include(clinic_image_router.urls)),
    path('',include(staff_image_router.urls))
]