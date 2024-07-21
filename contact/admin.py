from django.contrib import admin
from .models import Contact
from rangefilter.filters import DateRangeFilter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'email',
        'subject',
        'message',
    ]
    list_filter = ((
        'created_date',
        DateRangeFilter
    ),)