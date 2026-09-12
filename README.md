# Hangarin: Task & To-Do Manager

Hangarin is a simple web application built with Django that helps users organize their daily tasks, manage priorities, add notes, and break down large goals into smaller subtasks.

## Features

- **Task management** — create tasks with a title, description, deadline, status, category, and priority.
- **Subtasks** — break a task down into smaller, trackable steps.
- **Notes** — attach free-form notes to any task.
- **Categories & Priorities** — organize tasks by area (Work, School, Personal, Finance, Projects) and urgency (high, medium, low, critical, optional).
- **Admin dashboard** — full CRUD access with search and filtering for every model.

## Tech Stack

- Python 3.10
- Django 5.1.15
- SQLite (default database)
- Faker (test data generation)

## Entity Relationship

- `Priority` → `Task` (one-to-many)
- `Category` → `Task` (one-to-many)
- `Task` → `SubTask` (one-to-many, via `parent_task`)
- `Task` → `Note` (one-to-many)



