from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Messages

admin.site.register(Room)
admin.site.register(Messages)
admin.site.register(Topic)