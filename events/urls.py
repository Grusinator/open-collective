from django.urls import path

from .views import create_event, calendar_view, events_list_view, event_signup, event_signoff

urlpatterns = [
    path('create/', create_event, name='create_event'),
    path('calendar/', calendar_view, name='calendar'),
    path('events/', events_list_view, name='events_list'),
    path('signup/<int:event_id>/', event_signup, name='event_signup'),
    path('signoff/<int:event_id>/', event_signoff, name='event_signoff'),
]
