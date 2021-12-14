from django.urls import path,include
from . import views

app_name = 'parking_lot'

urlpatterns = [
    path('list/',
         views.parking_slot_list,
         name='parking_slot_list'),
    path('detail/<int:id>/',
         views.parking_slot_detail,
         name='parking_slot_detail'),
    path('create/',
         views.CreateParkingSlotView.as_view(),
         name='parking_slot_create'),
    path('<int:slot_number>/edit',
         views.EditParkingSlotView.as_view(),
         name='parking_slot_edit'),
    path('<int:slot_number>/delete',
         views.DeleteParkingSlotView.as_view(),
         name='parking_slot_delete'),
    path('<int:slot_number>/reservation/create',
         views.CreateReservationView.as_view(),
         name='reservation_create'),
    path('<int:slot_number>/reservation/<int:pk>/edit',
         views.EditReservationView.as_view(),
         name='reservation_edit'),
    path('<int:slot_number>/reservation/<int:pk>/delete',
         views.DeleteReservationView.as_view(),
         name='reservation_delete'),
]