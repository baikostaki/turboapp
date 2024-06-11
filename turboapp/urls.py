"""
URL configuration for turboapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from turboapp_users import views as user_views
from . import views

# from django.contrib.auth.views import LoginView


urlpatterns = [
    path("tracker/", include("expense_tracker.urls")),
    # re_path(r"^accounts/", include("django.contrib.auth.urls")),
    path("users/", view=include("turboapp_users.urls")),
    path("admin/", admin.site.urls),
    # path("register/", user_views.RegisterView.as_view(), name="register"),
    # path("login/", user_views.LoginView.as_view(), name="login"),
    path("", views.HomeView.as_view(), name="project_home"),
]

# urlpatterns += [
#  ]
