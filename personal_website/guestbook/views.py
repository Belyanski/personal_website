from django.shortcuts import render
from django.http import HttpResponse


def guestbook(request):
    return render(request, 'guestbook/guestbook.html')

def guest_entries(request):
    return render(request, 'guestbook/guest_entries.html')
