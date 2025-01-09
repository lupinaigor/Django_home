from django.urls import path
from .views import create_car, update_car, delete_car, get_all_cars, get_single_car

urlpatterns = [
    path('create', create_car),
    path('<int:pk>/', get_single_car),
    path('update/<int:pk>/', update_car),  # Для оновлення
    path('delete/<int:pk>/', delete_car),  # Для видалення
    path('all/', get_all_cars),  # Для отримання всіх об'ектів
]