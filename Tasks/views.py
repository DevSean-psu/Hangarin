from django.views.generic import ListView
from .models import Task


class HomePageView(ListView):
    model = Task
    template_name = "Tasks/home.html"
    context_object_name = "tasks"