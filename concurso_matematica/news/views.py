from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from .filters import NoticeFilter
from django.core.paginator import Paginator

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
                sub.main_comment = get_object_or_404(MainComment, pk=int(request.POST.get('main_comment_pk')))
                sub.save()
            else:
                return redirect('login')
            return redirect('new',pk)
    else:
        return render(request, 'news/new.html', context)

def upvote_main(request, pk):
    main = get_object_or_404(MainComment, pk=pk)
    main.upvotes+=1
    main.save()
    return redirect(request.META.get('HTTP_REFERER'))

def upvote_sub(request, pk):
    sub = get_object_or_404(SubComment, pk=pk)
    sub.upvotes+=1
    sub.save()
    return redirect(request.META.get('HTTP_REFERER'))

def downvote_main(request, pk):
    main = get_object_or_404(MainComment, pk=pk)
    main.downvotes+=1
    main.save()
    return redirect(request.META.get('HTTP_REFERER'))

def downvote_sub(request, pk):
    sub = get_object_or_404(SubComment, pk=pk)
    sub.downvotes+=1
    sub.save()
    return redirect(request.META.get('HTTP_REFERER'))
    
def list_news_view(request):
    news = Notice.objects.all()
    f = NoticeFilter(request.GET, queryset=news)
    paginator = Paginator(f.queryset, 6)
    page = paginator.get_page(request.GET.get('page',1))


    cxt = {
        'news': page,
        'filter': f,
    }
    return render(request, 'news/main.html', context=cxt)


def tag_click_view(request,tag_name):
    tag = Tag.objects.filter(name=tag_name)
    news = Notice.objects.filter(tag = tag)

    return render(request,'news/click_filter.html', context = {'news':news})

def create_notice(request):
    form = NoticeForm()
    if request.method == "GET" and request.GET:
        form = NoticeForm(request.GET, request.FILES)
        if form.is_valid():
            form.save()
            print('it worked')
            return redirect('home')
        else:

            print('No funciono')
            print(request.FILES)
            print(form.errors)
            return redirect('home')


    return render(request, 'news/create_notice.html', context={'form':form})
