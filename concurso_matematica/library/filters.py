import django_filters
from .models import HistoryPost

class HistoryPostFilter(django_filters.Filter):
    name = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model =  Notice
        fields =  {
            'name':['icontains'],
            'content':['icontains']
        }