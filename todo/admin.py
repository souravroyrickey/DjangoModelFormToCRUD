from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Task)
class AdminConfig(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created']
