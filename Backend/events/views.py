from rest_framework import viewsets, filters
from .models import Event
from .serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EventFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('day_event')
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = EventFilter
    filterset_fields = ('date_from', 'date_to')
    search_fields = ['title']
