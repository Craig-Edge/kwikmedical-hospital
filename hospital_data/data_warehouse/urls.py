from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)

urlpatterns = [
    path('api/hospitals/', HospitalViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/hospitals/<int:pk>/', HospitalViewSet.as_view({'get': 'retrieve'})),
]
