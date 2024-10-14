from django.shortcuts import render
from django.http import request
from django.http import request, HttpResponse

# Create your views here.
rooms = [
    {"id":1, "name": "python"},
    {"id":2, "name": "backend developers"},
    {"id":3, "name": "frontend developers"},
    {"id":4, "name": "scala with spark"},
]

def home(request:request) -> HttpResponse:
    context = {"rooms": rooms}
    template = "base/home.html"
    return render(request=request, template_name=template, context=context)


def room(request:request, id:str) -> HttpResponse:
    room = None
    for r in rooms:
        if r["id"] == int(id):
            room = r
    context = {"room": room}
    template = "base/room.html"
    return render(request=request, template_name=template, context=context)