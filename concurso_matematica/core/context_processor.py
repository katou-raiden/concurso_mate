from .models import Notification
from django.db.models import Q

def get_user_notifications(request):
    
    main_query = 'Notifications.objects.filter({0})'
    
    if hasattr(request.user, 'student'):
        Q_object = Q(role='professor')
        main_query.format('Q_object')
        result = eval(main_query)

    elif hasattr(request.user, 'professor'):
        Q_object = Q(role='student')
        main_query.format('Q_object')
        result = eval(main_query)
    
    all_notifications = Notification.objects.filter(role='all')
    
    try:
        all_notifications += result
    
    finally:
        return {
            'notifications' : all_notifications,
        }


