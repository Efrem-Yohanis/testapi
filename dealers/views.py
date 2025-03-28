from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dealer1
from .serializers import DealerSerializer

@api_view(['POST'])
def add_dealer(request):
    """Add a dealer to the database."""
    serializer = DealerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_dealers(request):
    """Retrieve the list of dealers."""
    dealers = Dealer1.objects.all()
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_dealer(request, dealer_id):
    """Update an existing dealer."""
    dealer = get_object_or_404(Dealer1, DealerId=dealer_id)
    serializer = DealerSerializer(dealer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_all_dealers(request):
    """Delete all dealers from the database."""
    Dealer1.objects.all().delete()
    return Response({'message': 'All dealers have been deleted.'}, status=status.HTTP_204_NO_CONTENT)
