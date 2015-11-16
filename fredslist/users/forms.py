from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'phone_number')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_date["email"]
        if commit:
            user.save()
        return user
