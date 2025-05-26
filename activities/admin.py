from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'resource_type', 'resource_id', 'timestamp')
    list_filter = ('action', 'resource_type')
    search_fields = ('user__email', 'resource_type', 'resource_id')