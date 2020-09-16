from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Comentario, Tema
from . import forms

# Create your views here.


def forum_main_view(request):
    arts = Post.objects.all()
    temas = Tema.objects.all()
    return render(request, 'forum/main.html', context={'arts': arts, 'temas':temas})


def forum_detail_view(request,id):
    obj = get_object_or_404(Post, id=id)
    comentarios = obj.comentarios.all()
    form = forms.ComentForm()
    if request.method == 'POST':
        form = forms.ComentForm(request.POST)
        if form.is_valid:
            cont = form.data['contenido']
            coment = Comentario(usuario=request.user, contenido=cont, post=obj)
            coment.save()
            return redirect('forum_detail', id=id)
    else:
        return render(request, 'forum/detail.html', context={'art': obj,'comentarios':comentarios,'form':form})


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
    temas = Tema.objects.all()
    tema = get_object_or_404(Tema, id=id)

    return render(request, 'forum/filter.html', context={'arts': arts, 'temas': temas, 'tema':tema})