from django.shortcuts import render
from django.http import HttpResponse


def guestbook(request):
    return render(request, 'guestbook/guestbook.html')
