from django import forms
from . import models 

class RoomForm(forms.ModelForm):
    
    class Meta:
        model = models.Room
        fields = ['host', 'topic', 'name']
