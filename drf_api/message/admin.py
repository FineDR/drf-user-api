from django.contrib import admin
from .models import Message
from api.models import UserTB
from conversation.models import Conversation
from django.utils.html import format_html

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender_id', 'message_preview', 'sent_at')
    list_filter = ('sent_at', 'conversation')
    search_fields = ('conversation__id', 'sender_id__username', 'message_description')
    readonly_fields = ('sent_at',)
    ordering = ('-sent_at',)


    list_per_page = 20
    fieldsets = (
        ('Message Details', {
            'fields': ('conversation', 'sender_id', 'message_description')
        }),
        ('Metadata', {
            'fields': ('sent_at',)
        }),
    )

    def message_preview(self, obj):
        return format_html('<span>{}</span>', obj.message_description[:50] + "...")
    message_preview.short_description = 'Message Preview'

    class Media:
        css = {
            'all': ('grappelli/css/grappelli.css',)
        }
        js = ('grappelli/js/grappelli.js',)
