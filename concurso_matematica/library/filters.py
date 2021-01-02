import django_filters
from .models import HistoryPost
from .models import Video

class HistoryPostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label="title", field_name="title", lookup_expr='icontains')
    content = django_filters.CharFilter(label="content", field_name="content", lookup_expr='icontains')

    class Meta:
        model =  HistoryPost
        fields =  (
            'title',
            'content',
        )

class VideoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='title')
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains', label='user')
    tags = django_filters.CharFilter(field_name='tag__name', lookup_expr='iexact', label='tags')
    playlist = django_filters.CharFilter(field_name='playlist__name', lookup_expr='icontains', label='playlist')

    class Meta:
        model = Video 
        fields = (
            'title', 
            'user', 
            'tags', 
            'playlist'
            )
        
