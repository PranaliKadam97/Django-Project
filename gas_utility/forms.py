from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer', 'request_type', 'details', 'attachment']

class UpdateRequestStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status', 'resolved_at']
