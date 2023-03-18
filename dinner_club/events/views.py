from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date

from .calendar_utils import month_calendar
from .models import DinnerClubEvent
from .forms import DinnerClubEventForm


def home(request):
    return render(request, 'events/home.html')


@login_required
def create_event(request):
    if request.method == 'POST':
        form = DinnerClubEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user
            event.save()
            return redirect('home')
    else:
        form = DinnerClubEventForm()
    return render(request, 'events/create_event.html', {'form': form})


@login_required
def calendar_view(request):
    today = date.today()
    events = DinnerClubEvent.objects.filter(date__year=today.year, date__month=today.month)
    weeks = month_calendar(today.year, today.month)
    return render(request, 'events/calendar.html', {'weeks': weeks, 'events': events})
