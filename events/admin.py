from django.contrib import admin

# Register your models here.
from events.models import Event, Guest
admin.site.register(Event)
admin.site.register(Guest)

#(sozdavat testovie tablici v admin panele)
#
# # Register your models here.
from events.models import Event, Guest
#
admin.site.register(Event)
admin.site.register(Guest)
