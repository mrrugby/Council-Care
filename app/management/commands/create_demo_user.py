import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from app.models import Employee  

class Command(BaseCommand):
    help = "Create or update demo user"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.environ.get("DEMO_USERNAME", "demo")
        password = os.environ.get("DEMO_PASSWORD")

        if not password:
            self.stderr.write(
                self.style.ERROR("DEMO_PASSWORD environment variable not set")
            )
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"is_employee": True}
        )

        user.is_employee = True
        user.is_technician = False
        user.is_admin = False
        user.set_password(password)
        user.save()

        Employee.objects.get_or_create(user=user)

        self.stdout.write(
            self.style.SUCCESS(
                f"{'Created' if created else 'Updated'} demo user"
            )
        )
