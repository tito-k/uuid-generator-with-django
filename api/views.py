from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Uuid
from .serializers import UuidSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def add_and_show_uuid(self):
    Uuid.objects.create()
    queryset = Uuid.objects.order_by('-timestamp')
    response = UuidSerializer(queryset, many=True).data
    return Response(data=response, status=status.HTTP_200_OK)