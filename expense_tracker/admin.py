from django.contrib import admin
from .models import Expense, Category, SubCategory


class CategoryAdmin(admin.ModelAdmin):  # type: ignore
    def __str__(self):
        return "Categories (__str__ in admin.py)"


admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(SubCategory)
