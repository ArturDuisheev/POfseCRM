from django.contrib import admin
from .models import Project, Client


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name_project', 'status', 'stars', 'date_created')
    list_filter = ('status', 'stars', 'date_created')
    search_fields = ('name_project',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
