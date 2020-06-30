from django_filters import rest_framework as filters
from .models import Event


class EventFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="day_event", lookup_expr='gte')
    date_to = filters.DateFilter(field_name="day_event", lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['date_from', 'date_to', 'lastday', 'lastweek', 'lastmonth']
