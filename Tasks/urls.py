from django.urls import path
from .views import (
    HomePageView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView,
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PriorityListView, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    path('subtasks/', SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add/', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtasks/<int:pk>/edit/', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtasks/<int:pk>/delete/', SubTaskDeleteView.as_view(), name='subtask-delete'),

    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/add/', NoteCreateView.as_view(), name='note-add'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('priorities/', PriorityListView.as_view(), name='priority-list'),
    path('priorities/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('priorities/<int:pk>/edit/', PriorityUpdateView.as_view(), name='priority-update'),
    path('priorities/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),
]