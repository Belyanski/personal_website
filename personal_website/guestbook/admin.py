from django.contrib import admin
from .models import GuestBookEntry

@admin.register(GuestBookEntry)
class GuestBookEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'message')
    date_hierarchy = 'timestamp'

