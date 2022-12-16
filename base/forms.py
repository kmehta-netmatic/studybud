from django.forms import ModelForm
from . import models 
from django.contrib.auth.models import User, Group


class RoomForm(ModelForm):
    
    class Meta:
        model = models.Room
        fields = ['host', 'topic', 'name', 'description']

class MessageForm(ModelForm):
    
    class Meta:
        model = models.Messages
        fields = ['body']

class UserForm(ModelForm):
    
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email']