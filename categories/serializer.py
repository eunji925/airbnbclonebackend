from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    # Category 필드 중에 어떤 부분을 보여줄 지 명시해줘야 한다.
    # serializer에게 name 과 kind 가 JSON으로 어떻게 표현되는지 설명한다.
    pk = serializers.IntegerField()
    name = serializers.CharField(required = True)
    kind = serializers.CharField()