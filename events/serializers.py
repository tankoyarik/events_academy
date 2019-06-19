from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from events.models import Event, Guest
from rest_framework_jwt.settings import api_settings

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields ="__all__"
        # exclude = ('events',)



class EventGuestsSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"


class CustomJWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(username=attrs.get("username")).first()
        if user_obj is not None:
            credentials = {
                self.username_field: attrs.get(self.username_field),
                "password": password,
            }
            if all(credentials.values()):
                try:
                    user = User.objects.get(
                        username__iexact=credentials[self.username_field]
                    )
                    if not user.is_active:
                        msg = "User account is disabled."
                        raise serializers.ValidationError(msg)
                except User.DoesNotExist:
                    pass

                user = authenticate(**credentials)
                if user:
                    payload = jwt_payload_handler(user)

                    return {"token": jwt_encode_handler(payload), "user": user}
                else:
                    msg = "Unable to log in with provided credentials."
                    raise serializers.ValidationError(msg)

            else:
                msg = f'Must include "{self.username_field}" and "password".'
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = "Account with this email/username does not exists"
            raise serializers.ValidationError(msg)
