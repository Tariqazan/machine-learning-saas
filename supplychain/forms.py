from django import forms
from .models import *


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['vehicle','date','message']
        widgets = {'date' : forms.DateInput(attrs={'type':'date'})}