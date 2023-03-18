from django.contrib.auth.models import User
from django.db import models


class DinnerClubEvent(models.Model):
    name = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(User, related_name='attendees', blank=True)

    def __str__(self):
        return self.name