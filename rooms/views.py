from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer

# /api/v1/rooms/amenities
class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True,)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data = request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data,)
        else:
            return Response(serializer.errors)


# /api/v1/rooms/amenities/1
class AmenityDetail(APIView):

    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)
        # 위처럼 쓰거나 아래처럼 1줄이거나 결국 같은 의미이다.
        # return Response(AmenitySerializer(self.get_object(pk),).data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer =  AmenitySerializer(amenity, data = request.data, partial = True)
        # partial = True : 사용자가 일부만 업데이트 할 수 있다.
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data,)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many = True,)
        return Response(serializer.data)


class RoomDetail(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        room = Room.objects.get(pk = pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)

# templetes 사용하기
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Room

# # Create your views here.
# def see_all_rooms(request):
#     rooms = Room.objects.all()
#     return render(
#         request, 
#         "all_rooms.html",
#         {"rooms" : rooms, "title": "this title comes from django!"}
#     )

# def see_one_room(request, room_pk):
#     try:
#         room = Room.objects.get(pk=room_pk)
#         return render(request, "room_detail.html", {"room" : room})
#     except Room.DoesNotExist:
#         return render(request, "room_detail.html", {"not_found" : True})