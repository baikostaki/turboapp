# from django.shortcuts import render
from typing import Any, Dict
from django.http import HttpResponse, request
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "turboapp/home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
