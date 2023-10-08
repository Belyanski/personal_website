from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('about/', include('about.urls', namespace='about')),
    path('education/', include('education.urls', namespace='education')),
    path('guestbook/', include('guestbook.urls', namespace='guestbook')),
    path('guest_entries/', include('guestbook.urls',
                                   namespace='guest_entries')),
    path('projects/', include('projects.urls', namespace='projects')),
]
