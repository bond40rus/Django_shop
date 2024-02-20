from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int,
                            help='UserID')  # pk первичный ключ вместо id чтобы не ругалась программа (принято писать в jango) принимаем аргумент из консоли

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(
            pk=pk).first()  # фильтр вместо get не выведет ошибок если такого персонажа нет first() - покажет первого если их несколько
        self.stdout.write(f'{client}')
