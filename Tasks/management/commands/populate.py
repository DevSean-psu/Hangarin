import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from Tasks.models import Task, SubTask, Note, Category, Priority


class Command(BaseCommand):
    help = "Populates the database with fake Task, SubTask, and Note data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not categories or not priorities:
            self.stdout.write(self.style.ERROR(
                "Add Category and Priority records first via /admin/."
            ))
            return

        for _ in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                category=random.choice(categories),
                priority=random.choice(priorities),
            )

            for _ in range(random.randint(1, 3)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=5),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                )

            for _ in range(random.randint(1, 2)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

        self.stdout.write(self.style.SUCCESS("Database populated successfully."))