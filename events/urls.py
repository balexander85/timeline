from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.TimelineView.as_view(), name="timeline"),
]
