from django.db import models
from django.conf import settings
from cuser.models import AbstractCUser


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
class User(AbstractCUser):
    pass

class Expense(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField("expense date")
    amount = models.DecimalField(max_digits=10, decimal_places = 2)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Category(models.Model):
    pass
