from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    # print(model_admin)
    # print(dir(request.user))
    # print(queryset)
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room) # Room Model 의 admin을 컨트롤 한다.
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = ("name", "price", "kind", "total_amenities", "rating", "owner", "created_at",)
    list_filter = ("country", "city", "pet_friendly", "kind", "amenities", "created_at",)

    search_fields = ("name", "price", "owner__username",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at", )
    # 수정 내역에서 해당 필드를 readonly 로 볼 수 있다.
    readonly_fields = ("created_at", "updated_at",)