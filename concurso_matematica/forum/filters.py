import django_filters as dfilter
from .models import Post

class PostFilter(dfilter.FilterSet):
    title = dfilter.CharFilter(field_name='title', lookup_expr='icontains', label="title")
    tags = dfilter.CharFilter(field_name='tag', lookup_expr='icontains', label="tags")
    user = dfilter.CharFilter(field_name='user', lookup_expr='contains', label="username")

    class Meta:
        model = Post
        fields = (
            'user__username',
            'tag__name',
            'title',
        )

    