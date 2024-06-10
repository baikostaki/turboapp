from django.shortcuts import render
from django.views.generic import TemplateView
from typing import Any


# Create your views here.
class LoginView(TemplateView):
    template_name = "tracker/login.html"


class RegisterView(TemplateView):
    template_name = "tracker/register.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ...
        return context
