from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from ..models import ParkingSlot
from .serializers import ParkingSlotSerializer, ReservationSerializer

class ParkingSlotListView(generics.ListAPIView):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer

class ParkingSlotDetailView(APIView):
    serializer_class = ParkingSlotSerializer
    def get(self,request,slot_number):
        slot = ParkingSlot.objects.get(slot_number=slot_number)
        result = ParkingSlotSerializer(slot).data
        result['reservations'] = []
        for reservation in slot.reservations.all():
            reservation_dict = ReservationSerializer(reservation).data
            result['reservations'].append(reservation_dict)

        return Response(result)

