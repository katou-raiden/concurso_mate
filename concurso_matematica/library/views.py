from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'library/main.html')

def videos_gallery_view(request):
    context = {}
    return render(request, 'library/videos.html', context=context)

def history_view(request):
    context = {}
    return render(request, 'library/history.html', context=context)