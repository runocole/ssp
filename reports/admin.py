from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'author', 'status', 'created_at')
    search_fields = ('team__name', 'author__email', 'status')
    list_filter = ('status', 'team')