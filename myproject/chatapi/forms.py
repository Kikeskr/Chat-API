from django import forms
from django.forms import ModelForm
from .models import User

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['tokens']