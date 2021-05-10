from django.shortcuts import render
from django.views.generic.list import ListView 
from .models import Task

class TaskList(ListView):
    model = Task
    template_name = 'base/tasks.html'
    context_object_name = "tasks"

