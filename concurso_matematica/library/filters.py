import django_filters
from .models import HistoryPost
from .models import Video

class HistoryPostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model =  HistoryPost
        fields =  {
            'title':['icontains'],
            'content':['icontains']
        }

class VideoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains', label='title', required=True)
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains', label='user', required=True)
    tags = django_filters.CharFilter(field_name='tag__name', lookup_expr='iexact', label='tags', required=True)
    playlist = django_filters.CharFilter(field_name='playlist__name', lookup_expr='icontains', label='playlist', required=True)

    class Meta:
        model = Video 
        fields = (
            'title', 
            'user', 
            'tags', 
            'playlist'
            )
        
