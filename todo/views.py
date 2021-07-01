from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from .models import TodoList


# Create your views here.

class Home(ListView):
    template_name = 'home.html'
    model = TodoList
    context_object_name = 'todo_list'  # if you not define this you will get the todo_object object_list
