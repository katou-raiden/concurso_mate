from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Comment, Answer
from core.models import Tag
from . import forms
from django.core.paginator import Paginator
from .filters import *

# Create your views here.
def test(request):
    form = forms.PostForm
    return render(request, 'forum/test.html',context={'form':form})

def forum_main_view(request):
    posts = Post.objects.all()
    return render(request, 'forum/main.html', context={'posts': posts})





def forum_detail_view(request,id):
    post = get_object_or_404(Post,id=id)
    answers = post.answers.all()
    post_comments = post.comments.all()
    if request.method == 'POST':
        answer_content = request.POST.get('content')
        answer = Answer(content = answer_content, user = request.user, post = post)
        answer.save()
        return redirect('forum_detail',id)
    else:
        context = {
            'post':post,
            'answers':answers,
            'post_comments':post_comments
        }
        return render(request,'forum/detail.html',context=context)


def forum_create_post_view(request):
    '''
        Campos del Formulario:
        title,content,tag
    '''
    tags = Tag.objects.all()
    form = PostForm(request.GET)
    if request.method == 'GET':
        title = request.GET.get('title')
        content = request.GET.get('content')
        tag = Tag.objects.get(id=request.GET.get('tag'))

        post = Post(user = request.user, title = title, content = content)
        post.save()
        post.tag.add(tag)
        return redirect('forum_main')
    else:
        return render(request, 'forum/create_post.html', context = {'tags':tags})

def forum_filter_view(request,id):
    tag = get_object_or_404(Tag, id=id)
    arts = Post.objects.filter(tag = tag)

    return render(request, 'forum/filter.html', context={'arts': arts, 'tag': tag})

def my_posts_view(request):
    posts = Post.objects.filter(user=request.user)

    return render(request, 'forum/my_posts.html', context={'posts':posts})

def my_posts_edit_view(request, id):
    post = get_object_or_404(Post,id=id)
    form = forms.PostForm(instance=post)
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid:
            post.title = form.data.get('title')
            post.content = form.data.get('content')
            obj = get_object_or_404(Tag,id=form.data.get('tag'))
            print(obj)
            post.tag.add(obj)
            post.save()
            message = 'Saved Successfully'
            return redirect('forum_main')
    else:
        return render(request, 'forum/edit_post.html', context={'post':post,'form':form})

def doubts_view(request):
    posts = Post.objects.all()
   
    form = PostFilter(request.GET, queryset=posts)
    paginator = Paginator(form.qs, 7)
    page = paginator.get_page(request.GET.get('page', 1))

    print(form.form)
      
    context = {
        'filter': form, 
        'posts': page,
        }
    
    
    return render(request, 'forum/doubts.html', context=context)

    def concursos_view(request):
        qs = Post.objects.filter(section='Concursos')

        context = {'posts':qs}

        return render(request, 'forum/concursos.html', context=context)