from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
