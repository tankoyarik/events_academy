from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import path, include

from events.views import (
    EventList,
    EventDetail,
    AllEventsGuests,
    EventGuests,
    EventCreate,
    GuestsListView,
    GuestDetailView,
)


urlpatterns = [
    path("events", EventList.as_view()),
    path("events/<int:pk>", EventDetail.as_view()),
    path("events/create", EventCreate.as_view()),
    path("events/guests", AllEventsGuests.as_view()),
    path("events/<int:pk>/guests", EventGuests.as_view()),
    path("guests", GuestsListView.as_view()),
    path("guests/<int:pk>", GuestDetailView.as_view())
    # path('events/<int:pk>/', my_view)
]
