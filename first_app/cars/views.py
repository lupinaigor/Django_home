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


@api_view(['GET'])
def get_single_car(request, pk):
    car = Car.objects.get(id=pk)
    serializer = CarSerializer(car)
    return Response(serializer.data)

# добавлення
@api_view(['PUT'])
def update_car(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Приклад запиту для Postman
# PUT-запит на URL /update/<id>/
#
# {
#     "brand": "Toyota",
#     "model": "Camry",
#     "year": 2023,
#     "price": 32000
# }



# видалення
@api_view(['DELETE'])
def delete_car(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

    car.delete()
    return Response({"message": f"Car with id {pk} was deleted successfully."}, status=status.HTTP_200_OK)

# Приклад запиту для Postman
# DELETE-запит на URL /delete/3/
# Має бути відповідь:
# {
#     "message": "Car with id 3 was deleted successfully."
# }


# читання усіх
@api_view(['GET'])
def get_all_cars(request):
    cars = Car.objects.all()  # отримуємо всі об'екти Car
    serializer = CarSerializer(cars, many=True)  # Серіализуемо список об'ъ'ектів
    return Response(serializer.data, status=status.HTTP_200_OK)
# Приклад запиту для Postman
# GET-запит на URL /all/