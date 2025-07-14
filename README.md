# 🎟️ Event Booking System

A Django-based web application that allows users to view upcoming events, book seats, and receive confirmation — with full admin control over events and bookings.

---
<img width="1920" height="1080" alt="Screenshot 2025-07-14 124020" src="https://github.com/user-attachments/assets/e35741b7-2ac3-4b2d-b3a8-5a81bc86f8c0" />
<img width="1920" height="1080" alt="Screenshot 2025-07-14 120228" src="https://github.com/user-attachments/assets/8f4dcfcc-806a-43fd-84f0-65b33a132eb2" />
<img width="1920" height="1080" alt="Screenshot 2025-07-14 124702" src="https://github.com/user-attachments/assets/e98cb63a-1c39-4dd5-b3ab-8bd269c62cf1" />
<img width="1920" height="1080" alt="Screenshot 2025-07-14 124642" src="https://github.com/user-attachments/assets/18802970-3656-4459-9a35-f9e4723dd26f" />

## 🚀 Features

- ✅ View list of upcoming events
- ✅ Event detail page with booking form
- ✅ Automatically calculates available seats
- ✅ Sold-out events are clearly marked
- ✅ Booking confirmation page
- ✅ Admin dashboard for managing events and bookings
- ✅ Custom template filter: `seats_left`
- ✅ Context processor: next upcoming event
- ✅ Console email confirmation (for development)

---

## 🛠️ Tech Stack

- **Framework**: Django 5.2+
- **Database**: SQLite (default, easy to switch)
- **Backend**: Python 3.10
- **Frontend**: Basic Django templates (customizable)
- **Admin Panel**: Django admin
- **Auth**: Custom User Model based on `AbstractUser`

---

## 📁 Project Structure

event_booking_system/
├── event_booking_system/ # Django settings module
├── events/ # Main app (models, views, forms)
├── templates/ # HTML templates
│ └── events/
├── static/ # Static files (optional)
├── media/ # Media uploads (optional)
├── requirements.txt
└── manage.py

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/event-booking-system.git
cd event-booking-system
2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Apply migrations and create a superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
5. Run the development server
python manage.py runserver

🧪 Testing the Features
Visit: http://127.0.0.1:8000/ to view the event list.

Book an event to trigger the confirmation logic.

Check the console output for simulated confirmation emails.

Visit: http://127.0.0.1:8000/admin/ for full admin functionality.
🧩 Custom Template Filter
Custom filter seats_left shows the number of seats left for an event.

File: events/templatetags/custom_filters.py
@register.filter
def seats_left(event):
    return event.seats_left()
Usage:
<p>Seats left: {{ event|seats_left }}</p>

🧠 Context Processor
Adds the next upcoming event globally:

File: events/context_processors.py

def next_upcoming_event(request):
    next_event = Event.objects.filter(date__gte=now()).order_by('date').first()
    return {'next_event': next_event}
Included in TEMPLATES → context_processors in settings.py.

📚 Resources Used
-Django Documentation

-Django Admin

-Custom Template Filters
