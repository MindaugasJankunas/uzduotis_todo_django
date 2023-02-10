from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'due', 'status', 'user')
    list_filter = ('status', 'user')
    search_fields = ('title', 'date', 'due')


admin.site.register(Task, TaskAdmin)

