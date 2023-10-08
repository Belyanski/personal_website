from django.urls import path

from . import views

app_name = 'guestbook'

urlpatterns = [
    path('', views.guestbook, name='guestbook'),
    path('guest_entries/', views.guest_entries, name='guest_entries'),
]
