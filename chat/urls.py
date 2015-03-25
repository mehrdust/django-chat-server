
from django.conf.urls import include, patterns, url
import socketio.sdjango

socketio.sdjango.autodiscover()

urlpatterns = patterns("chat.views",
    url("^socket\.io", include(socketio.sdjango.urls)),
    url("^$", "rooms", name="rooms"),
    url("^create/$", "create", name="create"),
    url("^(?P<slug>.*)$", "room", name="room"),
)
