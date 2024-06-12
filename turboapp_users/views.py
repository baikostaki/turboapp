from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from typing import Any
from django.contrib.auth import login, authenticate, logout
from turboapp_users.forms import RegistrationForm, LoginForm


# Create your views here.
class LoginView(FormView):
    template_name = "turboapp_users/forms/login_form.html"
    form_class = LoginForm
    success_url = reverse_lazy("project_home")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)  # type: ignore
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid email and/or password.")
            return self.form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ...
        return context


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


class LogoutView(RedirectView):
    url = reverse_lazy("project_home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
