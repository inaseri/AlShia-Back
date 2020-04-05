from rest_framework.permissions import AllowAny
# rest framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import viewsets


# serializer imports
from .serializers import CategoriesSerializer

# model imports
from .models import wp_term_taxonomy


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_categories_list(request):
    """
        This code bloc use for get list of categories from db.
    """
    if request.method == 'GET':
        parents_categories = wp_term_taxonomy.objects.all().filter(parent=0, taxonomy='category')
        print("parents category is:", parents_categories)
        serializer = CategoriesSerializer(parents_categories, many=True)
        return Response(serializer.data)
