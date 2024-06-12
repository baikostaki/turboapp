from django.urls import reverse_lazy
from django.views.generic import FormView
from typing import Any
from django.contrib.auth import login, authenticate
from turboapp_users.forms import RegistrationForm


# Create your views here.
class LoginView(FormView):
    template_name = "turboapp_users/forms/login_form.html"


class RegisterView(FormView):
    template_name = "turboapp_users/forms/registration_form.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("project_home")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ...
        return context
