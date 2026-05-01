from django.contrib import admin
from .models import Skill, Project, Publication


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order']
    list_editable = ['featured', 'order']
    list_filter = ['category', 'featured']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'venue', 'year', 'order']
    list_editable = ['order']
    list_filter = ['year']
