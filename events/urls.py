from django.urls import path

from events.views import (
    EventList,
    EventDetail,
    AllEventsGuests,
    EventGuests,
    GuestsListView,
    GuestDetailView,
    EventCreate,
)


urlpatterns = [
    path("events", EventList.as_view()),
    path("events/create", EventCreate.as_view()),
    path("events/<int:pk>", EventDetail.as_view()),
    path("events/guests", AllEventsGuests.as_view()),
    path("events/<int:pk>/guests", EventGuests.as_view()),
    path("guests", GuestsListView.as_view()),
    path("guests/<int:pk>", GuestDetailView.as_view()),
]
