from django.urls import path
from .views import create_car

urlpatterns = [
    path('create', create_car),
    # path('<int:pk>/', get_single_car),
]