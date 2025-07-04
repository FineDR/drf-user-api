from django.contrib import admin
from .models import Conversation
from product.models import Product
from api.models import UserTB

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('moto', 'buyer', 'status', 'started_at', 'conversation_status')
    list_filter = ('status', 'started_at')
    search_fields = ('moto__title', 'buyer__username')
    ordering = ('-started_at',)

    list_per_page = 20
    fieldsets = (
        ('Conversation Details', {
            'fields': ('moto', 'buyer', 'status')
        }),
        ('Metadata', {
            'fields': ('started_at',)
        }),
    )

    def conversation_status(self, obj):
        return obj.get_status_display()
    conversation_status.short_description = 'Status'

    class Media:
        css = {
            'all': ('grappelli/css/grappelli.css',)
        }
        js = ('grappelli/js/grappelli.js',)
