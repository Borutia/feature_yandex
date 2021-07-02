from django.core.management import BaseCommand

from reports import tasks


class Command(BaseCommand):
    help = """Запуск фоновых задач"""

    def handle(self, *args, **options):
        tasks.send_email_link_task.delay()
        tasks.send_report_task.delay()
        tasks.send_report_period_task.delay()
