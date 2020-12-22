import django_filters
from .models import HistoryPost

class HistoryPostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model =  HistoryPost
        fields =  {
            'title':['icontains'],
            'content':['icontains']
        }