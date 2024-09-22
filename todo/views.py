from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_delete.html"
    success_url = reverse_lazy("task_list")
