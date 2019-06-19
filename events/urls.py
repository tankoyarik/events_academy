from django.urls import path, include

from events.views import EventList, EventDetail, AllEventsGuests, EventGuests

urlpatterns = [
    path("events", EventList.as_view()),
    path("events/<int:pk>", EventDetail.as_view()),
    path("events/guests", AllEventsGuests.as_view()),
    path("events/<int:pk>/guests", EventGuests.as_view()),
    # path('events/<int:pk>/', my_view)
]
