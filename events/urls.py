from django.urls import path, include

from events.views import EventList

urlpatterns = [
    path('events', EventList.as_view()),
]