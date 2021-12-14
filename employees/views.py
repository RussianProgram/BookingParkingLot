from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class EmployeeRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('parking_lot:parking_slot_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)

        return result

class EmployeeLoginView(LoginView):
    def get_success_url(self):
        super().get_success_url()
        return reverse_lazy('parking_lot:parking_slot_list')

class EmployeeLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('parking_lot:parking_slot_list')
    def get_template_names(self):
        return 'registration/logged_out.html'