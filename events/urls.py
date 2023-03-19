from django.urls import path, include
from .views import home, create_event, calendar_view, events_list_view

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_event, name='create_event'),
    path('calendar/', calendar_view, name='calendar'),
    path('events/', events_list_view, name='events_list'),
]
