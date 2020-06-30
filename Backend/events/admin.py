from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'day_event', 'title', 'body']
    search_fields = ('title', 'body')
    list_filter = ('day_event',)


admin.site.register(Event, EventAdmin)
