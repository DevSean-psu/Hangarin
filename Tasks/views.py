from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm


class HomePageView(ListView):
    model = Task
    template_name = "Tasks/home.html"
    context_object_name = "tasks"


class TaskListView(ListView):
    model = Task
    template_name = "Tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 5


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "Tasks/task_form.html"
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "Tasks/task_form.html"
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "Tasks/task_confirm_delete.html"
    success_url = reverse_lazy('task-list')