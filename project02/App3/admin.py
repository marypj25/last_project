from django.contrib import admin

from .models import *

# admin.site.register(Item)

@admin.register(my_site)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_title', 'page_nav', 'page_nav_position', 'page_content', 'current_date']
    list_display_links = ['id','page_title', ]
    list_editable = ['page_nav', 'page_nav_position',]
    search_fields = ['page_content',]
    list_filter = ['page_title', 'page_nav']
    list_per_page = 15


