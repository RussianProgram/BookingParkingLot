
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parking-lot/',include('parking_lot.urls', namespace='parking_lot')),
    path('employees/',include('employees.urls')),
    path('api/',include('parking_lot.api.urls')),
]
