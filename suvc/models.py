from django.db import models
from django.contrib import admin

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)
    body  = models.TextField()
    timestam = models.DateTimeField()

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','body','timestam']
admin.site.register(News,NewsAdmin)