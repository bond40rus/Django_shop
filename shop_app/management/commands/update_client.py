from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Update user name byid."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int,
                            help='UserID')  # принимаем тут два аргумента, можно больше, чтобы изменить id имя
        parser.add_argument('phone', type=str, help='new_number_phone_client')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone = kwargs.get('phone')
        client = Client.objects.filter(pk=pk).first()
        client.phone = phone
        client.save()
        self.stdout.write(f'{client}')
