from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .calendar_utils import month_calendar
from .forms import DinnerClubEventForm
from .models import DinnerClubEvent


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
    return render(request, 'create_event.html', {'form': form})


@login_required
def calendar_view(request):
    today = date.today()
    events = DinnerClubEvent.objects.filter(date__year=today.year, date__month=today.month)
    weeks = month_calendar(today.year, today.month)
    return render(request, 'calendar.html', {'weeks': weeks, 'events': events})


@login_required
def events_list_view(request):
    events = DinnerClubEvent.objects.all()
    return render(request, 'events_list.html', {'events': events})


@login_required
def event_signup(request, event_id):
    event = get_object_or_404(DinnerClubEvent, pk=event_id)
    event.attendees.add(request.user)
    event.save()
    return redirect('events_list')


@login_required
def event_signoff(request, event_id):
    event = get_object_or_404(DinnerClubEvent, pk=event_id)
    event.attendees.remove(request.user)
    event.save()
    return redirect('events_list')
