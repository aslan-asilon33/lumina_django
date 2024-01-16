from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardList.as_view(), name='dashboard_list'),
]