from django.shortcuts import render
from .forms import *
# Create your views here.

def create_notification_view(request):
    form = NotificationForm()
    

    if request.method == 'GET':
        form = NotificationForm(request.GET)
        notification = form.save(commit=False)
        
        if notification.role == 'all':
            pass
        elif notification.role == 'student':
            pass
        elif notification.role == 'professor':
            pass
            
    context = {
        'form': form,
    }    
    
    return render(request, 'notifications/create_notification.html', context) 