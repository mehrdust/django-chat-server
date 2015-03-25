from socketio import socketio_manage

from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from chat.models import ChatRoom
# from chat.sockets import ChatNamespace

def rooms(request, template="rooms.html"):
    """
    Homepage - lists all rooms.
    """
    context = {"rooms": ChatRoom.objects.all()}
    # return render(request, template, context)
    print context
    return HttpResponse(context)


def room(request, slug, template="room.html"):
    """
    Show a room.
    """
    context = {"room": get_object_or_404(ChatRoom, slug=slug)}
    # return render(request, template, context)


def create(request):
    """
    Handles post from the "Add room" form on the homepage, and
    redirects to the new room.
    """
    pass
    # name = request.POST.get("name")
    # if name:
    #     room, created = ChatRoom.objects.get_or_create(name=name)
    #     return redirect(room)
    # return redirect(rooms)
