from django.contrib.auth.models import PermissionsMixin
from django.db import models
from cuser.models import AbstractCUser  # type: ignore
from django.contrib.auth.models import Group as BaseGroup


class TurboappUser(AbstractCUser, PermissionsMixin):
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    pass


class TurboappGroup(BaseGroup):
    class Meta:
        verbose_name = "group"
        verbose_name_plural: str = "groups"
        proxy = True
