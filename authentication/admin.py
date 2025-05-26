from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'firstName', 'lastName', 'role', 'team', 'createdAt')
    list_filter = ('role', 'team')
    search_fields = ('email', 'firstName', 'lastName')