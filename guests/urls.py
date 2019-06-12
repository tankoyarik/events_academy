from django.urls import path, include

from events.views import ,

#(PK = ID)
urlpatterns = [
    path('guests', EventList.as_view()),
    path('guests/<int:pk>', EventDetail.as_view())
]