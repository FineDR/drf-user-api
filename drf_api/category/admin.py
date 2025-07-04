from django.contrib import admin
from .models import Category
from api.models import UserTB

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_by', 'created_at', 'created_by_username')
    list_filter = ('created_at', 'created_by')
    search_fields = ('category_name', 'created_by__username')
    ordering = ('-created_at',)
    list_per_page = 20
    fieldsets = (
        ('Category Details', {
            'fields': ('category_name', 'created_by')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

    def created_by_username(self, obj):
        return obj.created_by.email
    created_by_username.short_description = 'Created By'

    class Media:
        css = {
            'all': ('grappelli/css/grappelli.css',)
        }
        js = ('grappelli/js/grappelli.js',)
