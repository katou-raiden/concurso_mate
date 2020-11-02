from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from .filters import NoticeFilter
# Create your views here.

def new_view(request, pk):
    main_form = MainCommentForm(prefix='main')
    sub_form = SubCommentForm(prefix='sub')
    new = get_object_or_404(Notice,pk=pk)
    comments = MainComment.objects.filter(notice = new)
    context = {
        'main_form':main_form,
        'sub_form':sub_form,
        'new':new,
        'comments':comments
    }
    if request.method == 'POST':
        main_form = MainCommentForm(request.POST,prefix='main')
        sub_form = SubCommentForm(request.POST, prefix='sub')

        if main_form.is_valid():
            main = main_form.save(commit=False)
            if request.user.is_authenticated:
                main.user = request.user
                main.notice = new
                main.save()
            else:
                return redirect('login')    
            return redirect('new',pk)
        elif sub_form.is_valid():
            sub = sub_form.save(commit=False)
            if request.user.is_authenticated:
                sub.user = request.user
                sub.save()
            else:
                return redirect('login')
            return redirect('new',pk)
    else:
        return render(request, 'news/new.html', context)

def list_news_view(request):
    news = Notice.objects.all()
    f = NoticeFilter(request.GET, queryset=news)
    cxt = {
        'news':news,
        'filter': f,
    }
    return render(request, 'news/main.html', context=cxt)


def add_new_view(request):
    form = NoticeForm()

    if request.method == 'POST':
        form = NoticeForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            new = form.save(commit = False)
            if request.user.is_authenticated:
                new.user = request.user
                new.save()
                return redirect('home')
            else:
                return redirect('login')
        else:
            return redirect('add_new')
    else:
        return render(request, 'news/add_new.html', context={'form':form})

def tag_click_view(request,tag_name):
    tag = Tag.objects.filter(name=tag_name)
    news = Notice.objects.filter(tag = tag)

    return render(request,'news/click_filter.html', context = {'news':news})