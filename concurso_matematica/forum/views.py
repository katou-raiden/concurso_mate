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
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_main')
        else:
            return redirect(forum_post_view(request))
    else:
        return render(request, 'forum/post.html',context={'form': form})

def forum_filter_view(request,id):
    arts = Post.objects.filter(id=id)
    temas = Tag.objects.all()
    tema = get_object_or_404(Tag, id=id)

    return render(request, 'forum/filter.html', context={'arts': arts, 'temas': temas, 'tema':tema})