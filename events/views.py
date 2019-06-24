from django.contrib.auth.models import User


# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event, Guest
from events.serializers import (
    EventSerializer,
    EventGuestsSerializer,
    GuestSerializer,
    GuestSerializerEvents,
    UserSerializer,
)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class EventDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response(data={"message": "Not found"}, status=404)
        serializer = EventSerializer(instance=event)

        return Response(data=serializer.data)

    def delete(self, request, pk):
        try:
            event = Event.objects.get(id=pk).delete()
        except Event.DoesNotExist:
            return Response(data={"message": "Not found"}, status=404)

        return Response(data={"message": "Object deleted successfully"}, status=204)


#
# ALready have this functionality inside ListCreate Api view
class EventCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        payload = request.data
        serializer = EventSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data={"message": "Invalid"}, status=400)


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
