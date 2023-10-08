from django.shortcuts import render


def custom_404(request, exception):
    template = 'core/404.html'
    return render(request, template, status=404)
