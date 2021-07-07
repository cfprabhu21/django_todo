from django.urls import path
from .views import Home, AddTodo

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create_todo/', AddTodo.as_view(), name='addtodo'),
]