from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('about/', include('about.urls', namespace='about')),
    path('education/', include('education.urls', namespace='education')),
    path('guestbook/', include('guestbook.urls', namespace='guestbook')),
    path('projects/', include('projects.urls', namespace='projects')),
]
