import django_filters
from .models import Notice

class NoticeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model =  Notice
        fields =  {
            'title':['icontains'],
            'content':['icontains']
        }