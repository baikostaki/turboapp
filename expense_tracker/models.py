from django.db import models
from django.conf import settings  # type: ignore


# class Profile(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )


class Expense(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField("expense date")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


class Category(models.Model):
    title = models.CharField(max_length=200, default="New Category")
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural: str = "Categories"


class SubCategory(models.Model):
    title = models.CharField(max_length=200, default="New Subcategory")
    description = models.CharField(max_length=200, null=True, blank=True)
    categories = models.ManyToManyField(Category)  # type: ignore

    class Meta:
        verbose_name_plural = "Subcategories"
