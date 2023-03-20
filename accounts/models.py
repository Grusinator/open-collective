from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    move_in_date = models.DateField(blank=True, null=True)
    move_out_date = models.DateField(blank=True, null=True)
    google_profile_picture = models.URLField(blank=True, null=True)
    google_refresh_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
