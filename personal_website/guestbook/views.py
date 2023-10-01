from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import GuestBookEntry
from .forms import GuestBookEntryForm  # Создайте эту форму

def guestbook(request):
    entries = GuestBookEntry.objects.order_by('-timestamp')
    paginator = Paginator(entries, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    return render(request, 'guestbook/guestbook.html', {'page': page})

def guest_entries(request):
    if request.method == 'POST':
        form = GuestBookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook:guestbook')
    else:
        form = GuestBookEntryForm()
    
    return render(request, 'guestbook/guest_entries.html', {'form': form})
