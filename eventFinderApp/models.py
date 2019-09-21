from django.conf import settings
from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    venue = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category', related_name= 'events')
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING, null = "True") # null: can have event with host
    #attendees = models.ManyToManyField(User, related_name = 'attending_events')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("eventFinderApp:event", kwargs={"pk": self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Account(models.Model):
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()