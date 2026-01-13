from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Config

# Register your models here.
@admin.register(Config)
class ConfigAdmin(TranslatableAdmin):
    list_display = ['id', 'name', 'updated']
    list_editable = ['name']

    def has_add_permission(self, request):
        return len(Config.objects.all())<1