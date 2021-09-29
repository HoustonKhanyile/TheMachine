from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm
from .models import Appear, Performance, Publicity

class AppsForm(ModelForm):
    class Meta:
         model = Appear
         fields = ['Show', 'Media', 'Episode', 'Date', 'Time', 'Producer', 'Producer_Email']
   

class Perform(ModelForm):
    class Meta:
        model = Performance
        fields = ['Event', 'Date', 'Start_Time', 'Time_Slot', 'Country', 'City', 'Venue']
        
class Public_R(ModelForm):
    class Meta:
        model = Publicity
        fields = ['Name', 'Media', 'Country', 'Date', 'Link']
        