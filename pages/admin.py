from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'created_at', 'author')
    search_fields = ('title', 'code', 'subtitle')
