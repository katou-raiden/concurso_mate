from django.http.response import HttpResponse
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from forum.models import Post
from news.models import Notice
from library.models import HistoryPost
from accounts.models import Completed_Exercise
from training.models import Exercise
from forum.forms import PostForm

# Create your views here.

def dashboard_view(request):
    qspost = Post.objects.all()
    qsnews = Notice.objects.all()
    qshist = HistoryPost.objects.all()
    qexercises = Exercise.objects.all()
    context = {'Posts':qspost, 'News':qsnews, 'HPost':qshist, 'Exerc':qexercises}
    return render(request, 'dashboard/dashboard.html', context=context)

def remove_post_view(request,pk):
    post = Post.objects.filter(pk=pk).delete()
    return redirect(request.META.get('HTTP_REFERER'))

def remove_Hpost_view(request,pk):
    hpost = HistoryPost.objects.filter(pk=pk).delete()
    return redirect(request.META.get('HTTP_REFERER'))

def remove_new_view(request,pk):
    new = Notice.objects.filter(pk=pk).delete()
    return redirect(request.META.get('HTTP_REFERER'))

def remove_exercise_view(request,pk):
    new = Exercise.objects.filter(pk=pk).delete()
    return redirect(request.META.get('HTTP_REFERER'))

def edit_post_view(request,pk):
    post = get_object_or_404(Post, pk = pk)
    form = PostForm(instance = post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return HttpResponse('Todo Bien')
        else:
            return render(request,'forum/create_post.html', context={'form':form, 'errors':form.errors})
    else:
        return render(request,'forum/create_post.html', context={'form':form})

def edit_Hpost_view(request,pk):
    Hpost = get_object_or_404(HistoryPost, pk = pk)
    form = PostForm(instance = Hpost)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = Hpost)
        if form.is_valid():
            form.save()
            return HttpResponse('Todo Bien')
        else:
            return render(request,'library/create_history.html', context={'form':form, 'errors':form.errors})
    else:
        return render(request,'library/create_history.html', context={'form':form})

def edit_New_view(request,pk):
    new = get_object_or_404(Notice, pk = pk)
    form = PostForm(instance = new)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = new)
        if form.is_valid():
            form.save()
            return HttpResponse('Todo Bien')
        else:
            return render(request,'news/create_notice.html', context={'form':form, 'errors':form.errors})
    else:
        return render(request,'news/create_notice.html', context={'form':form})

def edit_exercise_view(request,pk):
    ex = get_object_or_404(Exercise, pk = pk)
    form = PostForm(instance = ex)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = ex)
        if form.is_valid():
            form.save()
            return HttpResponse('Todo Bien')
        else:
            return render(request,'training/ex_post.html', context={'form':form, 'errors':form.errors})
    else:
        return render(request,'training/ex_post.html', context={'form':form})