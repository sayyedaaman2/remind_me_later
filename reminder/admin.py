from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'user', 'schedule_time', 'created_at', 'updated_at', 'status']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['message', 'user__username']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Reminder, ReminderAdmin)
