from django.views.generic import ListView

from source.tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = 'templates/task.html'


class TagListView(ListView):
    model = Tag
    template_name = 'templates/tags.html'
