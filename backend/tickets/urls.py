from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet,
    SubDepartmentViewSet,
    HospitalTicketViewSet,
    ITTicketViewSet,
)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'subdepartments', SubDepartmentViewSet, basename='subdepartment')
router.register(r'hospital-tickets', HospitalTicketViewSet)
router.register(r'it-tickets', ITTicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
