# photos/admin.py

from django.contrib import admin
from .models import Photo, Like

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'likes']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'session_key']

