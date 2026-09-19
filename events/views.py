from django.views.generic import ListView

from .models import Event


class TimelineView(ListView):
    model = Event
    template_name = "events/timeline.html"
    context_object_name = "events"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_data"] = self._build_timeline_json(context["events"])
        return context

    def _build_timeline_json(self, events):
        return {
            "title": {
                "text": {"headline": "Historical Timeline"},
            },
            "events": [self._event_to_slide(event) for event in events],
        }

    @staticmethod
    def _event_to_slide(event):
        slide = {
            "start_date": TimelineView._date_dict(event.start_date),
            "text": {
                "headline": event.title,
                "text": event.body,
            },
        }
        if event.end_date:
            slide["end_date"] = TimelineView._date_dict(event.end_date)
        if event.image:
            slide["media"] = {"url": event.image.url}
        return slide

    @staticmethod
    def _date_dict(date):
        return {"year": date.year, "month": date.month, "day": date.day}
