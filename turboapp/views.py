# from django.shortcuts import render
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


class HomeView(TemplateView):
    template_name = "home.html"
