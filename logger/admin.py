from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_address', 'device_type', 'device_model', 'device_brand', 'country', 'city')
    search_fields = ('ip_address', 'user_agent', 'device_model', 'device_brand')
    list_filter = ('device_type', 'country', 'timestamp')
    ordering = ('-timestamp',)