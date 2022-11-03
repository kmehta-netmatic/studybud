from django.forms import ModelForm
from . import models 

class RoomForm(ModelForm):
    
    class Meta:
        model = models.Room
        fields = ['host', 'topic', 'name', 'description']

class MessageForm(ModelForm):
    
    class Meta:
        model = models.Messages
        fields = ['body']