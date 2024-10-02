from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_rooms), # root 경로\
    path("<int:room_pk>", views.see_one_room)
    # <> : 우리가 받을 parameter의 데이터 타입:이름(원하는 것으로 지정 가능)
]