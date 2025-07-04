from django.contrib import admin
from .models import MotocycleImage
from django.utils.html import format_html

@admin.register(MotocycleImage)
class MotocycleImageAdmin(admin.ModelAdmin):
    list_display = (
        'get_title', 'get_price', 'get_category', 'get_status', 'get_posted_by', 
        'image_path', 'image_preview', 'action_buttons',
    )
    list_per_page = 20

    readonly_fields = ('uploaded_at',)  # ✅ Mark as readonly

    fieldsets = (
        ('Motocycle Image Details', {
            'fields': ('product','image', 'is_primary')
        }),
        # You can optionally show metadata like this
     
    )

    def get_title(self, obj):
        return obj.product.title if obj.product else "-"
    get_title.short_description = 'Title'

    def get_price(self, obj):
        return obj.product.price if obj.product else "-"
    get_price.short_description = 'Price'

    def get_category(self, obj):
        return obj.product.category.category_name if obj.product and obj.product.category else "-"
    get_category.short_description = 'Category'

    def get_status(self, obj):
        return obj.product.status if obj.product else "-"
    get_status.short_description = 'Status'

    def get_posted_by(self, obj):
        return obj.product.posted_by if obj.product else "-"
    get_posted_by.short_description = 'Posted By'

    def image_path(self, obj):
        return obj.image.name if obj.image else "No Image"
    image_path.short_description = 'Image Path'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image Preview"

    def action_buttons(self, obj):
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Delete</a>',
            f"/admin/motocycleimage/motocycleimage/{obj.pk}/change/",
            f"/admin/motocycleimage/motocycleimage/{obj.pk}/delete/"
        )
    action_buttons.short_description = "Actions"
