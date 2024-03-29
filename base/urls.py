from django.urls import path #path function triggers 
from . import views

urlpatterns = [
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('home/', views.home, name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('edit-room/<int:pk>/', views.updateRoom, name='edit-room'),
    path('delete-room/<int:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<int:pk>/', views.deleteComment, name='delete-message'),
    path('notAuthorized/', views.notAuthorized, name='notAuthorized'),
    path('user-profile/<int:pk>', views.userProfile, name='user-profile'),
    path('edit-user-profile/<int:pk>', views.userEditProfile, name='edit-user-profile'),
    path('edit-user-password/<int:pk>', views.userEditPassword, name='edit-user-password'),
]