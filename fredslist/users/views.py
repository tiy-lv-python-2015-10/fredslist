from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import RegistrationForm


class Register(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('list_locations')
    template_name = 'registration/register.html'