from .models import Event
from django.utils.timezone import now

def next_upcoming_event(request):
    next_event = Event.objects.filter(date__gte=now()).order_by('date').first()
    return {'next_upcoming_event': next_event}
