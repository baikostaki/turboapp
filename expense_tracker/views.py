# from django.shortcuts import render
from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.apps import apps


class HomeView(TemplateView):
    template_name = "expense_tracker/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context["app_alias"] = apps.get_app_config("turboapp_users")
        return context
