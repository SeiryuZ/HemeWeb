from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created', 'updated')
    readonly_fields = ('id', 'created', 'updated', 'status')
