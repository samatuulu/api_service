from django.views.generic import ListView

from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = 'task.html'


class TagListView(ListView):
    model = Tag
    template_name = 'tags.html'

