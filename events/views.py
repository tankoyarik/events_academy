from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from events.models import Event
from events.serializers import EventSerializer, EventGuestsSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventsGuestsList(generics.ListCreateAPIView):
    queryset = Event.objects.prefetch_related('guests').all()
    serializer_class = EventGuestsSerializer


class EventGuests(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.prefetch_related('guests').all()
    serializer_class = EventGuestsSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
