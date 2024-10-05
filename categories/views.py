from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerializer

@api_view()
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response(serializer.data,)