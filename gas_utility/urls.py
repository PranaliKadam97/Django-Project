from django.urls import path
from .views import (
    SubmitServiceRequestView,
    TrackServiceRequestView,
    ManageServiceRequestView,
    UpdateRequestStatusView,
)

app_name = 'gas_utility'

urlpatterns = [
    path('submit-request/', SubmitServiceRequestView.as_view(), name='submit-request'),
    path('track-requests/', TrackServiceRequestView.as_view(), name='track-requests'),
    path('manage-service-requests/', ManageServiceRequestView.as_view(), name='manage-service-requests'),
    path('update-status/<int:pk>/', UpdateRequestStatusView.as_view(), name='update-status'),
]
