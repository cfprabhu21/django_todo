from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, View, ListView
from django.views import View
from .models import TodoList
from .forms import TodoForm


# Create your views here.

class Home(ListView):
    template_name = 'home.html'
    model = TodoList
    context_object_name = 'todo_list'  # if you not define this you will get the todo_object object_list


class AddTodo(View):
    form_class = TodoForm

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('todo:home'))
