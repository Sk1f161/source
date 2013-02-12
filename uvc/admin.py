__author__ = 'Sk1f'
from django.contrib import admin
from suvc.models import News

#test
class NewsAdmin(admin.ModelAdmin):
    list_display = ['Title','body','timestamp']
    ordering = ['title']
admin.site.register(NewsAdmin,News)