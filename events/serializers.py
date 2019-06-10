from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from events.models import Event, Guest


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class EventGuestsSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"


