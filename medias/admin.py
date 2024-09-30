from django.contrib import admin
from .models import Photo, Video

@admin.register(Photo)
class Photoadmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class Videoadmin(admin.ModelAdmin):
    pass