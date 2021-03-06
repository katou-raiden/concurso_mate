"""concurso_matematica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from dashboard.views import dashboard_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('forum/', include('forum.urls')),
    #path('tinymce/', include('tinymce.urls')),
    path('news/', include('news.urls')),
    path('library/', include('library.urls')),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('training/', include('training.urls')),
    path('dash/', include('dashboard.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('tags_input/', include('tags_input.urls', namespace='tags_input')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
