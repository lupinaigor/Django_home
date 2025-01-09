from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def create_car(request):
    # print("Hello!")
    print("__data", request.data)
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET'])
# def get_single_car(request, pk):
#     car = Car.objects.get(id=pk)
#     serializer = CarSerializer(car)
#     return Response(serializer.data)