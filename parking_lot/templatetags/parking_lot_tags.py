from django import template
from django.http import HttpResponseNotFound
from ..models import Reservation
from datetime import datetime


register = template.Library()

@register.filter(name='day_filter')
def filter_by_day(query_object, day):
    today = datetime.now()
    query_object.filter(booked_until__lt=today).delete()
    previous_daytime = Reservation.get_previous_daytime()
    if day.day > previous_daytime.day:
        qs = query_object.filter(booked_from__day__lte=day.day, booked_until__day__gte=day.day)
        return qs
    else:
        raise HttpResponseNotFound('This object no longer exist')
