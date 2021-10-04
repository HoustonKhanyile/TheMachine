from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm
from .models import Appear, Performance, Publicity, Bookings, Profile

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

class Book(ModelForm):
    class Meta:
        model = Bookings
        fields = ['Artist', 'Event', 'Name_of_Event', 'Date', 'Time_Slot', 'Set_Time', 'Country','City', 'Venue', 'Promoter', 'Promoter_Email']

class Profiles(ModelForm):
    class Meta:
        model = Profile
        fields = ['Name', 'Last_Name', 'Address_Line_1', 'Address_Line_2', 'Postcode', 'State', 'Area', 'Email', 'Country', 'State_Region']        