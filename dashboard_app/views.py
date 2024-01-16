from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
import requests
from django.shortcuts import render
from django.http import JsonResponse

class DashboardList(ListView):
    template_name = 'dashboard_list.html'
    def get_queryset(self):
        # Make a request to your API
        api_url = 'http://localhost:8000/api/users'
        response = requests.get(api_url)

        if response.status_code == 200:
            # Process the API response and return the data
            data = response.json()
            return data
        else:
            # Handle API error, you might want to customize this based on your needs
            return []

    def get(self, request, *args, **kwargs):
        # Override the get method to handle the API response
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)