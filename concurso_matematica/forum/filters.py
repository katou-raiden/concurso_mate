import django_filters as dfilter
from .models import Post

class PostFilter(dfilter.FilterSet):
    title = dfilter.CharFilter(lookup_expr='icontains')
    tags = dfilter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['user__username']

    