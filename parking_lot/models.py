from django.db import models
from django.urls import reverse
from employees.models import Employee
from django.db.models import F,Q
import datetime


class ParkingSlot(models.Model):
    slot_number = models.PositiveIntegerField()

    def __str__(self):
        return f'Parking Slot No. {self.slot_number}'

    def get_absolute_url(self):
        return reverse('parking_lot:parking_slot_detail',
                       args=[self.slot_number])



class Reservation(models.Model):
    slot = models.ForeignKey(ParkingSlot,
                                     related_name='reservations',
                                     on_delete=models.CASCADE)
    booked_by = models.OneToOneField(Employee,
                                     related_name='booked_parking_slot',
                                     on_delete=models.CASCADE)
    booked_from = models.DateTimeField()
    booked_until = models.DateTimeField()

    @property
    def expiration(self):
        if self.booked_until > self.booked_until.today():
            return True
        return False

    def __str__(self):
        return f'Booked from {self.booked_from} || until {self.booked_until} || by {self.booked_by.user.username}'

    @staticmethod
    def get_previous_daytime():
        now = datetime.datetime.now()
        prev_date = now - datetime.timedelta(1)
        prev_time = now.time().max
        prev_datetime = datetime.datetime.combine(prev_date, prev_time)
        return prev_datetime

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='start_date_before_end_date',
                check=Q(booked_from__lt=F("booked_until"))
            )
        ]


