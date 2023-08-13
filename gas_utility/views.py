from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from .models import ServiceRequest
from .forms import ServiceRequestForm, UpdateRequestStatusForm

class SubmitServiceRequestView(CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'gas_utility/submit_service_request.html'
    success_url = '/thank-you/'

class TrackServiceRequestView(ListView):
    model = ServiceRequest
    template_name = 'gas_utility/track_service_request.html'
    context_object_name = 'service_requests'

class ManageServiceRequestView(ListView):
    model = ServiceRequest
    template_name = 'gas_utility/manage_service_request.html'
    context_object_name = 'service_requests'

class UpdateRequestStatusView(UpdateView):
    model = ServiceRequest
    form_class = UpdateRequestStatusForm
    template_name = 'gas_utility/update_request_status.html'
    success_url = '/manage-service-requests/'
