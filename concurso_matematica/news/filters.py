import django_filters
from .models import Notice

class NoticeFilter(django_filters.Filter):
    name = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model =  Notice
        fields =  {
            'name':['icontains'],
            'content':['icontains']
        }