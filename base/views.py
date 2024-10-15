from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import request, HttpResponse
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

def home(request: request) -> HttpResponse:
    query = request.GET.get("q") if request.GET.get("q") != None else ""
    ## search functionality
    rooms = Room.objects.filter(Q(topic__name__icontains=query) | Q(name__icontains=query) | Q(description__icontains=query))
    # Q can allows the searching on multiple conditions, not necessarily match all condition like (topic__name__icontains=query, name__icontains=query)
    #__ to query to parent  ## icontains whatever values in  ##contains = case sensitive

    room_count = rooms.count()

    topics = Topic.objects.all()

    topic_count = len(list(set([room.topic for room in rooms])))

    context = {"rooms": rooms, "room_count": room_count, "topics":topics, "topic_count":topic_count}
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