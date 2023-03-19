from django.db import models

from accounts.models import CustomUser


class DinnerClubEvent(models.Model):
    name = models.CharField(max_length=255)
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(CustomUser, related_name='attendees', blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name