from django.contrib import admin
from .models import ParkingSlot, Reservation


class ReservationInline(admin.StackedInline):
    model = Reservation

@admin.register(ParkingSlot)
class AdminParkingSlot(admin.ModelAdmin):
    list_display = ['slot_number']
    inlines = [ReservationInline]

@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    list_display = ['slot',
                    'booked_by',
                    'booked_from',
                    'booked_until']
    list_filer = ['booked_from',
                   'booked_until']

    search_fields = ['booked_by']
