from django.urls import path
from .views import create_car, update_car, delete_car, get_all_cars

urlpatterns = [
    path('create', create_car),
    # path('<int:pk>/', get_single_car),
    path('update/<int:pk>/', update_car),  # Добавлено для обновления
    path('delete/<int:pk>/', delete_car),  # Новый маршрут для удаления
    path('all/', get_all_cars),  # Новый маршрут для получения всех объектов
]