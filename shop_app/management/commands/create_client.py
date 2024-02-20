from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Сергей Бонд', email='sb@mail.ru', phone='9105860186', address='marksa 100 / 43')
        client.save()
        self.stdout.write(f'{client}')
