from django.urls import path, include

from events.views import EventList, EventGuests, EventsGuestsList, EventDetail

urlpatterns = [
    path('events', EventList.as_view()),
    path('event/<int:pk>', EventDetail.as_view()),
    path('event/<int:pk>/guests', EventGuests.as_view()),
    path('events/guests', EventsGuestsList.as_view())
]
