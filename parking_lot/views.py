from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .models import ParkingSlot,Reservation
#from .forms import ReservationCreateForm

import datetime
from .services import to_datetime

"""Views for list and detail parking slots"""

def parking_slot_detail(request,id):
    slot = get_object_or_404(ParkingSlot,slot_number=id)

    return render(request,
                  'slot_detail.html',
                  {'slot':slot})


def parking_slot_list(request):
    parking_slot_list = ParkingSlot.objects.all()
    day = datetime.date.today()

    context = {"parking_slot_list":parking_slot_list,
                   "day":day}

    response = render(request,
                      'slot_list.html',
                      context=context)

    if request.method == 'POST':
        if request.POST['day'] != "":
            day = request.POST['day']
            new_day = datetime.datetime.strptime(day,"%Y-%m-%d")
            context.update({"day":new_day})
            return render(request,
                          'slot_list.html',
                          context=context)
        else:
            return response

    return response

"""Views for creating/updating/deleting parking slots"""

class ChangeParkingSlotMixin(PermissionRequiredMixin):
    model = ParkingSlot
    fields = ['slot_number']
    success_url = reverse_lazy('parking_lot:parking_slot_list')
    template_name = 'slot_form.html'

class CreateParkingSlotView(ChangeParkingSlotMixin,generic.CreateView):
    permission_required = 'parking_lot.add_parkingslot'

class EditParkingSlotView(ChangeParkingSlotMixin, generic.UpdateView):
    permission_required = 'parking_lot.change_parkingslot'

    def get_object(self, queryset=None):
        obj = ParkingSlot.objects.get(slot_number=self.kwargs['slot_number'])
        return obj

class DeleteParkingSlotView(PermissionRequiredMixin,generic.DeleteView):
    model = ParkingSlot
    success_url = reverse_lazy('parking_lot:parking_slot_list')
    template_name = 'slot_delete_confirm.html'
    permission_required = 'parking_lot.delete_parkingslot'


    def get_object(self, queryset=None):
        obj = ParkingSlot.objects.get(slot_number=self.kwargs['slot_number'])
        return obj

"""Views for creating/updating/deleting reservations"""

class ReservationMixinView(LoginRequiredMixin,generic.FormView):
    model = Reservation
    success_url = reverse_lazy('parking_lot:parking_slot_list')
    template_name = 'reservation/reservation_form.html'
    fields = ['booked_from','booked_until']

    def get_queryset(self):
        slot_resns = Reservation.objects.filter(slot__slot_number=self.kwargs['slot_number'])
        return slot_resns

    def post(self, request, *args, **kwargs):
        booked_from_this = to_datetime(request.POST['booked_from'])
        booked_until_this = to_datetime(request.POST['booked_until'])
        slot_reservations = self.get_queryset()
        is_valid = False
        if slot_reservations.exists():
            for r in slot_reservations:
                if r.booked_by.user != request.user:
                    if (booked_from_this < r.booked_from.timestamp()) \
                            and (booked_until_this < r.booked_from.timestamp()):
                        is_valid = True
                    elif booked_from_this > r.booked_until.timestamp():
                        is_valid = True
                    else:
                        is_valid = False
                        break
                else:
                     is_valid = True
          else:
            is_valid = True

        if is_valid:
            return self.form_valid(self.get_form())
        else:
            raise ValidationError('Dont interrupt others reservation')


class CreateReservationView(ReservationMixinView,LoginRequiredMixin, generic.CreateView):
    def get_object(self, queryset=None):
        object = ParkingSlot.objects.get(slot_number=self.kwargs['slot_number'])
        return object

    def form_valid(self, form):
        form.instance.booked_by = self.request.user.employee
        form.instance.slot = self.get_object()
        return super().form_valid(form)


class EditReservationView(ReservationMixinView,LoginRequiredMixin, generic.UpdateView):
    def form_valid(self, form):
        form.instance.id = self.kwargs['pk']
        form.instance.booked_by = self.request.user.employee
        form.instance.slot = ParkingSlot.objects.get(slot_number=self.kwargs['slot_number'])
        form.instance.booked_from = self.request.POST['booked_from']
        form.instance.booked_until = self.request.POST['booked_until']
        return super().form_valid(form)


class DeleteReservationView(LoginRequiredMixin, generic.DeleteView):
    model = Reservation
    success_url = reverse_lazy('parking_lot:parking_slot_list')
    template_name = 'reservation/reservation_delete_confirm.html'



