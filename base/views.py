from django.shortcuts import render, redirect
from django.http import request
from django.http import request, HttpResponse
from .models import Room
from .forms import RoomForm

# Create your views here.
# rooms = [
#     {"id":1, "name": "python"},
#     {"id":2, "name": "backend developers"},
#     {"id":3, "name": "frontend developers"},
#     {"id":4, "name": "scala with spark"},
# ]


def home(request: request) -> HttpResponse:
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    template = "base/home.html"
    return render(request=request, template_name=template, context=context)


def room(request: request, id: str) -> HttpResponse:
    room = Room.objects.get(id=id)
    context = {"room": room}
    template = "base/room.html"
    return render(request=request, template_name=template, context=context)


def createRoom(request: request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {"form": form}
    return render(request=request, template_name="base/room_form.html", context=context)


def updateRoom(request:request, id:str):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room) # prefill the form with instance room
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request=request, template_name="base/room_form.html", context=context)



def deleteRoom(request:request, id:str):
    room = Room.objects.get(id=id)
    if request.method == "POST":
        room.delete()
        return redirect("home") 
    context = {"object":room}
    return render(request=request, template_name="base/delete.html", context=context)


def deleteMessage(request:request):
    pass