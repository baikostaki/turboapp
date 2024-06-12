from django.urls import path, include

from . import views

urlpatterns = [
    # path("users", include(django.contrib.auth.urls)),  # type: ignore
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
]
