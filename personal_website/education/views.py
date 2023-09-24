from django.shortcuts import render
from django.http import HttpResponse


def education(request):
    return render(request, 'education/education.html')
