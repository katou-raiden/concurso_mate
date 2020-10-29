import django_filters
from .models import Notice

class NoticeFilter(django_filters.Filter):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model =  Notice
        fields =  {
            'tag__name':['iexact']
        }