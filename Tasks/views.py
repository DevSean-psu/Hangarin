from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm


class HomePageView(ListView):
    model = Task
    template_name = "Tasks/home.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.count()
        context["pending_count"] = Task.objects.filter(status="Pending").count()
        context["progress_count"] = Task.objects.filter(status="In Progress").count()
        context["completed_count"] = Task.objects.filter(status="Completed").count()
        context["total_categories"] = Category.objects.count()
        context["total_priorities"] = Priority.objects.count()
        return context


# --- Task ---
class TaskListView(ListView):
    model = Task
    template_name = "Tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = ["title", "deadline", "status"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title"


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


# --- SubTask ---
class SubTaskListView(ListView):
    model = SubTask
    template_name = "Tasks/subtask_list.html"
    context_object_name = "subtasks"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(title__icontains=query))
        return qs


class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('subtask-list')


class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('subtask-list')


class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = "Tasks/generic_confirm_delete.html"
    success_url = reverse_lazy('subtask-list')


# --- Note ---
class NoteListView(ListView):
    model = Note
    template_name = "Tasks/note_list.html"
    context_object_name = "notes"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(content__icontains=query))
        return qs


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('note-list')


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('note-list')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "Tasks/generic_confirm_delete.html"
    success_url = reverse_lazy('note-list')


# --- Category ---
class CategoryListView(ListView):
    model = Category
    template_name = "Tasks/category_list.html"
    context_object_name = "categories"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "Tasks/generic_confirm_delete.html"
    success_url = reverse_lazy('category-list')


# --- Priority ---
class PriorityListView(ListView):
    model = Priority
    template_name = "Tasks/priority_list.html"
    context_object_name = "priorities"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs


class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('priority-list')


class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = "Tasks/generic_form.html"
    success_url = reverse_lazy('priority-list')


class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = "Tasks/generic_confirm_delete.html"
    success_url = reverse_lazy('priority-list')