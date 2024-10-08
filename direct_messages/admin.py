from django.contrib import admin
from .models import ChattingRoom, Message

@admin.register(ChattingRoom)
class Roomadmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at", "updated_at",)
    list_filter = ("created_at",)

@admin.register(Message)
class Messageadmin(admin.ModelAdmin):
    list_display = ("text", "user", "ChattingRoom", "created_at",)
    list_filter = ("created_at",)