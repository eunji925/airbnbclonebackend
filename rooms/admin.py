from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room) # Room Model 의 admin을 컨트롤 한다.
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "kind", "owner", "created_at", "updated_at",)
    list_filter = ("country", "city", "pet_friendly", "kind", "amenities", "created_at", "updated_at",)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at", )
    # 수정 내역에서 해당 필드를 readonly 로 볼 수 있다.
    readonly_fields = ("created_at", "updated_at",)