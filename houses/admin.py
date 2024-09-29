from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    # 묶어 보기
    #fields = ("name", "address", ("price_per_night", "pets_allowed"))
    # admin 패널에 보이고 싶은 column 들의 list
    list_display = ("name", "price_per_night", "address", "pets_allowed",)
    # filtering
    list_filter = ("price_per_night", "pets_allowed")
    # 검색 
    #search_fields = ("address",) # search_fields = ("address__startswith") : 검색하는 텍스트로 시작하는 것만 검색
    # list 에서 선택 시 이동하게 만들기
    #list_display_links = ("name", "address",)
    # list화면에서 바로 list의 property 들을 수정할 수 있다.
    #list_editable = ("pets_allowed",) 