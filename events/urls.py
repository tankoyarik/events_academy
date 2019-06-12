from django.urls import path, include

from events.views import EventList, EventDetail, EventCreate

urlpatterns = [
    path('events', EventList.as_view()),
    path('events/<int:pk>', EventDetail.as_view()),
    path('events/create', EventCreate.as_view())
    # path('events/<int:pk>/', my_view)
]
