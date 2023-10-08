from django import forms
from django.urls import reverse

from .models import GuestBookEntry


class GuestBookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestBookEntry
        fields = ['name', 'message']

    def get_success_url(self):
        return reverse('guestbook')

    class Meta:
        model = GuestBookEntry
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-95', 'id': 'inputPassword3'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].initial = ''
