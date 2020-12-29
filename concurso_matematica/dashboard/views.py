from django.shortcuts import render
from django.contrib.auth.models import User
from forum.models import Post
from news.models import Notice
from library.models import HistoryPost
from accounts.models import Completed_Exercise

# Create your views here.

def dashboard_view(request):
    qspost = Post.objects.all()
    qsnews = Notice.objects.all()
    qshist = HistoryPost.objects.all()
    context = {'Posts':qspost, 'News':qsnews, 'HPost':qshist}
    return render(request, 'dashboard/dashboard.html', context=context)