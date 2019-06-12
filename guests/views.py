from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event
from events.serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(APIView):

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(data={"message":"Not Found"}, status=404)
        serializer = EventSerializer(Instance=event)
        return Response(data=serializer.data)

    def post(self,request, pk):
        payload = request.data
        serializer = EventSerializer(data=payload)
        if serializer.is_valid():
            event = Event(moderator_id=payload['moderator'],
                          title=payload['title'],
                          description=payload['description'],
                          image_url=payload['image_url'],
                          max_guest_limit=payload['max_guest_limit'])
            event.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data={"message":"Invalid"}, status=400)



    def put(self,request,pk):
        return Response(data={"hello": "put"})

    def delete(self,request,pk):
        return Response(data={"hello": "delete"})
