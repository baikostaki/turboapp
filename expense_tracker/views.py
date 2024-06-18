# from django.shortcuts import render
from hmac import new
from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import temp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.conf import settings
from django.apps import apps

from expense_tracker.forms.expense_form import ExpenseForm
from expense_tracker.models import Expense, Category


class HomeView(TemplateView):
    template_name = "expense_tracker/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context["app_alias"] = apps.get_app_config("turboapp_users")
        return context


class CreateExpenseView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "expense_tracker/create_expense_form.html"
    success_url = reverse_lazy("expense_tracker_home")

    def get(self, request):
        form = ExpenseForm()
        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request):
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            if (
                "create_new_category" in request.POST
                and request.POST["create_new_category"] == "create"
            ):
                new_category_name = form.cleaned_data["new_category"]
                if new_category_name:
                    new_category, created = Category.objects.get_or_create(
                        name=new_category_name
                    )
                    form.instance.category = new_category
                    form.instance.save()
                    return redirect("add_expense")
            form.save()
            return redirect("expense_tracker/home")
        return render(request, template_name=self.template_name, context={"form": form})
