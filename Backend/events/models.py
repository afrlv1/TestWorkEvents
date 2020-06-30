from django.db import models


class Event(models.Model):
    day_event = models.DateField(u'Day of the event', help_text=u'Day of the event')
    title = models.CharField(u'Title', max_length=255, help_text=u'Title', blank=True, null=True)
    body = models.TextField(u'Textual Event', help_text=u'Textual Event', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
