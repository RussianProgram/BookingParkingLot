from rest_framework import serializers
from ..models import ParkingSlot, Reservation

class ParkingSlotSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    slot_number = serializers.IntegerField()

class ReservationSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    booked_from = serializers.DateTimeField()
    booked_until = serializers.DateTimeField()