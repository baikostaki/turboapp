from django.db import models
from django.conf import settings  # type: ignore
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=200, default="New Category")
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural: str = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length=200, default="New Subcategory")
    description = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.category.name} - {self.name}"  # type: ignore

    class Meta:
        verbose_name_plural = "Subcategories"


class Shop(models.Model):
    name = models.CharField(max_length=200, default="New Shop")
    description = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200)


class Expense(models.Model):
    name = models.CharField(max_length=200, default="New Expense")
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(default=date.today)  # type: ignore
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    categories = models.ManyToManyField(
        Category, through="ExpenseCategory", default="General"
    )
    shop = models.ForeignKey(Shop, null=True, blank=True, on_delete=models.CASCADE)


class ExpenseCategory(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
