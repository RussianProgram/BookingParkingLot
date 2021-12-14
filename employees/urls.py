from django.urls import path

from . import views

app_name = 'employees'

urlpatterns = [
    path('register/',
         views.EmployeeRegistrationView.as_view(),
         name='employee_registration'),
    path('login/',
         views.EmployeeLoginView.as_view(),
         name='employee_login'),
    path('logout/',
         views.EmployeeLogoutView.as_view(),
         name='employee_logout'),
]