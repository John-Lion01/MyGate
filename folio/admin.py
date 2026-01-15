from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Config, About

# Register your models here.
@admin.register(Config)
class ConfigAdmin(TranslatableAdmin):
    list_display = ['id', 'name', 'updated']
    list_editable = ['name']

    def has_add_permission(self, request):
        return len(Config.objects.all())<1

@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    list_display = ['id', 'updated']

    def has_add_permission(self, request):
        return not About.objects.exists()