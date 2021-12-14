from django.urls import path
from . import views as api_views

app_name = 'parking_lot'

urlpatterns = [
    path('list/',api_views.ParkingSlotListView.as_view()),
    path('detail/<int:slot_number>',api_views.ParkingSlotDetailView.as_view()),
]
