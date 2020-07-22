from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView

from main.models import Deal, AdvUser
from .serializers import DealSerializer

@api_view(['GET'])
def deals(request):
    if request.method == 'GET':
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)

class DealView(RetrieveAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer