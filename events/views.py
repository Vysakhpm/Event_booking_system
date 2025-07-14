from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Event
from .forms import BookingForm

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = BookingForm()
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})

def book_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if event.sold_out:
        return render(request, 'events/booking_confirmation.html', {'message': 'Sold Out'})

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.seats > event.seats_left():
                form.add_error('seats', 'Not enough seats available.')
            else:
                booking.event = event
                booking.save()
                if event.seats_left() <= 0:
                    event.sold_out = True
                    event.save()
                send_mail(
                    subject='Booking Confirmation',
                    message=f'Hi {booking.name}, your booking for {event.title} is confirmed.',
                    from_email='noreply@example.com',
                    recipient_list=[booking.email],
                    fail_silently=False,
                )
                return render(request, 'events/booking_confirmation.html', {'booking': booking})
    else:
        form = BookingForm()

    return render(request, 'events/event_detail.html', {'event': event, 'form': form})
