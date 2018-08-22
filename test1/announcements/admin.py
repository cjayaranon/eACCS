from django.contrib import admin
from .models import Announcement

# Register your models here.

class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
        'date_created',
        'input_text',
        'author',
        'post_status',
        'date_post'
    ]
    
    
    
admin.site.register(Announcement, AnnouncementsAdmin)