from django.contrib.auth.models import User


# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from events.models import Event, Guest
from events.serializers import (
    EventSerializer,
    EventGuestsSerializer,
    GuestSerializer,
    UserSerializer,
)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class AllEventsGuests(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all().prefetch_related("guests")
    serializer_class = EventGuestsSerializer


class EventGuests(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all().prefetch_related("guests")
    serializer_class = EventGuestsSerializer


class GuestsListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
