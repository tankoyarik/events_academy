from django.db import models

# Create your models here.
# charfield = string
#Cascade = если юзер удаляется, удаляются все юзеры(его посты)
from django.utils import timezone


class Event(models.Model):
    moderator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=200, blank=True, null=True)
    max_guest_limit = models.IntegerField(null=False, blank=False, default=10)
    date_created = models.DateTimeField(default=timezone.now, blank=False, null=False)
    start_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Guest(models.Model):
    event = models.ManyToManyField("Event", related_name="guests")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


