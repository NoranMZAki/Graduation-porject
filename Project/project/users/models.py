from django.db import models

from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
