from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import CommentForm,VideoForm,PlaylistForm
from .filters import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


#----------------Video Section----------------# 

#Video Detail View

def video_detail_view(request,pk):
    video = get_object_or_404(Video,id=pk)
    return render(request, 'library/video_detail.html',context = {'video':video} )

# Main View tendra no se si recuerdes los videos random y las playlists pues ahi los tienes esto seria
# tu video_gallery_view si lo consideras necesario cambiale el nombre

def videos_gallery_view(request):
    videos_random = Video.objects.filter(playlist=null)
    playlists = Playlist.objects.all()

    context = {'videosqs':videos_random, 'playlists':playlists}

    return render(request, 'library/video_main.html', context=context)

# Post Video View

def video_post_view(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST)
        video = form.save(commit=False)
        video.user = request.user
        video.playlist = None
        video.save()
        return redirect('videos')
    else:
        return render(request, 'library/video_post.html', {'form':form})

# Add Playlist

def playlist_add_view(request):
    form = PlaylistForm()
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        playlist = form.save(commit=False)
        playlist.user = request.user
        playlist.save()
        return redirect('videos')
    else:
        return render(request, 'library/playlist_add.html', {'form':form})

# Add Video to Playlist esto lleva validaciones de usuario postando vs usuario dueno de playlist

def add_to_playlist_view(request, playlist_pk):
    form = VideoForm()
    playlist = Playlist.objects.filter(pk=playlist_pk)
    if request.method == 'POST':
        form = VideoForm(request.POST)
        video = form.save(commit=False)
        video.user = request.user
        video.playlist = playlist
        video.save()
        return redirect('videos')
    else:
        return render(request, 'library/video_post.html', {'form':form})

#----------------End Video Section--------------------------#


def main_view(request):
    return render(request, 'library/main.html')

def history_view(request):
    h_posts = HistoryPost.objects.all()
    f = HistoryPostFilter(request.GET, queryset=h_posts)
    paginator = Paginator(f.queryset, 6)
    page = paginator.get_page(request.GET.get('page',1))
    context = { 
        'h_posts':page, 
        'filters': f,
        }
    return render(request, 'library/history.html', context=context)



def downloads_main_view(request):
    return render(request,'library/downloads_main.html')

def download_section_view(request,section):
    pass

#Terminar Esto despues de hacer el Formulario para Comments


def history_post_view(request,pk):
    post = get_object_or_404(HistoryPost,id=pk)
    comments = post.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('library')
        else:
            return HttpResponse('Error en el formulario')
    else:
        context = {
            'post':post,
            'comments':comments,
            'form':form
        }
        return render(request, 'library/history_post.html',context)


    context = {'post':post, 'comments':comments}
    return render(request, 'library/history.html', context=context)

def tag_click_view(request,tag_name):
    tag = Tag.objects.filter(name=tag_name)
    news = HistoryPost.objects.filter(tag = tag)

    return render(request,'news/click_filter.html', context = {'hps':hps})