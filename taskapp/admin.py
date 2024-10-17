from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')  
    list_filter = ('status',) 
    search_fields = ('title', 'description') 
    ordering = ('status', 'title')  

admin.site.register(Task, TaskAdmin)
