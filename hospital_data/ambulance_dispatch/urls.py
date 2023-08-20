from django.urls import path
from .views import AmbulanceDispatchViewSet, DispatchRequestViewSet

urlpatterns = [
    path('api/dispatch-ambulance/', AmbulanceDispatchViewSet.as_view({'post': 'create'}), name='dispatch-ambulance'),
    path('api/dispatch-requests/', DispatchRequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='dispatch-requests-list'),
    path('api/dispatch-requests/<str:pk>/', DispatchRequestViewSet.as_view({'patch': 'partial_update'}), name='dispatch-requests-detail'),
]
