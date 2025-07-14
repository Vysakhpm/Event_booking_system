from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, Booking, CustomUser

admin.site.register(CustomUser, UserAdmin)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'capacity', 'sold_out')
    search_fields = ('title',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'seats', 'created_at')
