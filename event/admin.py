#!/usr/bin/env python

from django.contrib import admin
from event.models import Event, Product

class EventAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'amount', 'product', 'value', 'notes')
    list_filter = ('timestamp', 'user', 'action', 'amount', 'product', 'value')
    search_fields = ['notes']

admin.site.register(Event, EventAdmin)
admin.site.register(Product)
