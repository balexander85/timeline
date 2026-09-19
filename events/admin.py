from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")
    list_filter = ("start_date",)
    search_fields = ("title", "body")
    date_hierarchy = "start_date"
    ordering = ("start_date",)
