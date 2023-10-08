from django.shortcuts import render


def education(request):
    return render(request, 'education/education.html')
