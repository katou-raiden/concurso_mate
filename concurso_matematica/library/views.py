from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CommentForm

# Create your views here.

def main_view(request):
    return render(request, 'library/main.html')

def history_main_view(request):
    h_posts = HistoryPost.objects.all()
    return render(request, 'library/history_main.html', context={'h_posts':h_posts})

def video_detail_view(request,pk):
    video = get_object_or_404(Video,id=pk)
    return render(request, 'library/video_detail.html',context = {'video':video} )

def downloads_main_view(request):
    return render(request,'library/downloads_main.html')

def download_section_view(request,section):
    pass

def videos_gallery_view(request):
    videos = Video.objects.all()
    context = {'videos':videos}
    return render(request, 'library/videos.html', context=context)

def history_view(request):
    context = {
        'history_posts': HistoryPost.objects.all()
    }
    return render(request, 'library/history.html', context)

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