from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    capacity = models.IntegerField()
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def seats_left(self):
        booked = sum(booking.seats for booking in self.booking_set.all())
        return self.capacity - booked

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    seats = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"
