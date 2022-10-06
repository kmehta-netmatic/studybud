from django.urls import path #path function triggers 
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('edit-room/<int:pk>/', views.updateRoom, name='edit-room'),
    path('delete-room/<int:pk>/', views.deleteRoom, name='delete-room'),
]