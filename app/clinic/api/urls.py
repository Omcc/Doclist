from django.urls import path,include

from . import views
from rest_framework.routers import DefaultRouter


from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/staffs$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]

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


router = CustomReadOnlyRouter()

router.register('clinics',views.ClinicView,basename='clinics')
router.register('staffs',views.StaffView,basename="clinics-staffs")

urlpatterns = [
    path('clinics/',clinic_list,name="clinic-list"),
    path('clinics/<int:pk>/',clinic_detail,name="clinic-detail"),
    path('clinics/staffs',staff_list,name="clinic-staff-list")
]