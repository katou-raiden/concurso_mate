from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Comment, Answer
from core.models import Tag
from .forms import *
from django.core.paginator import Paginator
from .filters import *

# Create your views here.

def forum_main_view(request):
    return render(request, 'forum/main.html')

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

def upvote_comment_post(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    voted = Comment.voted.all()
    if voted.filter(username=request.user):
        comment.votes_plus +=1
        comment.save()
    else:
        comment.votes_plus-=1
        comment.save() 
    return redirect(request.META.get('HTTP_REFERER'))

def downvote_comment_post(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    voted = Comment.voted.all()
    if voted.filter(username=request.user):
        comment.votes_minus +=1
        comment.save()
    else:
        comment.votes_minus-=1
        comment.save() 
    return redirect(request.META.get('HTTP_REFERER'))

def upvote_answer_post(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    voted = Comment.voted.all()
    if voted.filter(username=request.user):
        comment.votes_plus +=1
        comment.save()
    else:
        comment.votes_plus-=1
        comment.save() 
    return redirect(request.META.get('HTTP_REFERER'))

def downvote_answer_post(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    voted = Comment.voted.all()
    if voted.filter(username=request.user):
        comment.votes_minus +=1
        comment.save()
    else:
        comment.votes_minus-=1
        comment.save() 
    return redirect(request.META.get('HTTP_REFERER'))


def forum_create_post_view(request,section):
    '''
        Campos del Formulario:
        title,content,tag
    '''
    form = PostForm()
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        post.section = section
        post.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'forum/create_post.html', context = {'tags':tags,'form':form})

# Tag click filter

def forum_filter_view(request,id):
    tag = get_object_or_404(Tag, id=id)
    arts = Post.objects.filter(tag = tag)

    return render(request, 'forum/filter.html', context={'arts': arts, 'tag': tag})

#Esta view se incluiria en Dashboard , necesito que me confirmes lo de esta view y la que le sigue a esta
def my_posts_view(request):
    posts = Post.objects.filter(user=request.user)

    return render(request, 'forum/my_posts.html', context={'posts':posts})

#Esta View es mas bien para Dashboard
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

#Esta es la view general de las secciones
def section_view(request,section):
    posts = Post.objects.all()
    sections = ('doubts', 'support', 'contests')

    if section in sections:
        #Aqui podrias incluir logica para definir contextos en funcion de la seccion que sea
        
        posts = Post.objects.filter(section=section)
        form = PostFilter(request.GET, queryset=posts)
        paginator = Paginator(form.qs, 7)
        page = paginator.get_page(request.GET.get('page', 1))
        
        context = {
        'filter': form, 
        'posts': page,
            }

        return render(request, 'forum/doubts.html', context=context)

    #Ahora no me acuerdo del nombre de la excepcion codigo 404
    raise Exception('Seccion no encontrada')
    
