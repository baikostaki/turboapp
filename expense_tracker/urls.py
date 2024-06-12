from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="expense_tracker_home"),
]
