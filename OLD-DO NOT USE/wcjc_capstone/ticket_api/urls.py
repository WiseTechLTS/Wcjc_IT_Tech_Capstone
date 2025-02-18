# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ParentDepartmentViewSet,
    SubDepartmentViewSet,
    TicketViewSet,
    HospitalTicketViewSet,
)

router = DefaultRouter()
router.register(r'parent-departments', ParentDepartmentViewSet, basename='parentdepartment')
router.register(r'sub-departments', SubDepartmentViewSet, basename='subdepartment')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'hospital-tickets', HospitalTicketViewSet, basename='hospitalticket')

urlpatterns = [
    path('api/', include(router.urls)),
]
