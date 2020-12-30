import django_filters
from django import forms
from .models import Notice

class NoticeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')
    username = django_filters.CharFilter(field_name="user__username", lookup_expr='icontains')
    tags = django_filters.CharFilter(field_name="tag__name", lookup_expr='icontains', widget=forms.Textarea())

    class Meta:
        model =  Notice
        fields = ('title', 'user', 'tag')
        
        