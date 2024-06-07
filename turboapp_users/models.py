from django.db import models
from custom_user.models import AbstractEmailUser  # type: ignore


class TurboAppUser(AbstractEmailUser):
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    pass
