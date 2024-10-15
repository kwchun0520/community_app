from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# db tables


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    # do it auto when updated, auto_now takes snapshot on every time we save
    created = models.DateTimeField(auto_now_add=True)
    # do it auto when created, auto_now_add takes timestamp when we first save/created

    class Meta:
        ordering = ["-updated", "-created"] # desc order

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Django has built in user model
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # on_delete=models.SETNULL -> when someone is deleted the room, the room parameter is set to null
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]
