from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Comment, Tag, Answer
from . import forms

# Create your views here.


def forum_main_view(request):
    posts = Post.objects.all()
    temas = Tag.objects.all()
    return render(request, 'forum/main.html', context={'posts': posts, 'temas':temas})


def forum_detail_view(request,id):
    post = get_object_or_404(Post,id=id)
    answers = post.answers.all()
    post_comments = post.comments.all()
    if request.method == 'POST':
        answer_content = request.POST.get('content')
        print(answer_content)
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


def forum_post_view(request):
    '''
        Campos del Formulario:
        title,content,tag
    '''
    tags = Tag.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tag_id = request.POST.get('tag')
        post = Post(user = request.user, title = title, content = content, tag = Tag.objects.get(id=tag_id))
        post.save()
        return redirect('forum_main')
    else:
        return render(request, 'forum/post.html', context = {'tags':tags})

def forum_filter_view(request,id):
    tag = get_object_or_404(Tag, id=id)
    arts = Post.objects.all(tag = tag)

    return render(request, 'forum/filter.html', context={'arts': arts, 'tag': tag})