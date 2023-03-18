from django import forms

from .models import DinnerClubEvent


class DinnerClubEventForm(forms.ModelForm):
    class Meta:
        model = DinnerClubEvent
        fields = ['date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '60'}),
        }


