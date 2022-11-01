from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm
from django.db.models import Q
from django.template import loader

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets Learn Python'},
#     {'id': 2, 'name': 'Design With Me'},
#     {'id': 3, 'name': 'Frontend Developer'},
# ]

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except:
            messages.error(request, 'User does not exist')
        
            user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect(home)
        else:
            print(messages.error)
            messages.error(request, 'Username or password is incorrect')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    print(request)
    logout(request)
    print(request)
    return redirect(home)

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    context = {'page': page, 'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'base/login_register.html', context)


def notAuthorized(request):
    return render(request, 'base/not_authorized.html')

def home(request):
    search = request.GET.get('search_for') if request.GET.get('search_for') != None else ''
    #rooms = Room.objects.filter(host__username=search)
    rooms = Room.objects.filter(
        Q(topic__name__icontains=search) |
        Q(host__username__icontains=search) |
        Q(name__icontains=search) |
        Q(description__icontains=search)
        )
    topics = Topic.objects.all()
    users = User.objects.all()
    print(request.user.is_superuser)
    roomCount = len(rooms)
    context = {'rooms': rooms, 'topics': topics, 'users': users, 'search': search, 'roomCount': roomCount}
    return render(request, 'base/home.html', context)

def room(request, pk): #To populate URI with room id
    # room = None
    # for i in rooms:
    #     if i['id'] == pk:
    #         room = i
    rooms = Room.objects.get(id=pk)
    context = {'room': rooms}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'forms': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return redirect('notAuthorized')

    if request.method =='POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')         
    context = {'forms': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk) 

    if request.user != room.host:
        return redirect('notAuthorized')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})