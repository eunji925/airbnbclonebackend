from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    # Category 필드 중에 어떤 부분을 보여줄 지 명시해줘야 한다.
    # serializer에게 name 과 kind 가 JSON으로 어떻게 표현되는지 설명한다.
    pk = serializers.IntegerField(read_only = True) 
    # read_only = True : serializers에게 user가 보내지 않는 내용이라고 알려주는 것.
    name = serializers.CharField(required = True, max_length=50,)
    kind = serializers.ChoiceField(choices = Category.CategoryKindChoices.choices,)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance