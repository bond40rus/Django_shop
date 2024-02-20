from django.db import models

from datetime import date


# для миграции в базу данных таблиц в  терминале /**project
# python manage.py makemigrations
# python manage.py migrate

class Client(models.Model):  # наследуемся от класса model
    name = models.CharField(max_length=100)  # Создаем столбцы таблицы, id в django ставится автоматически
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_registration = models.DateTimeField(auto_now=True)

    def __str__(self):  # текстовое представление класса
        return f'User name: {self.name}, email:{self.email}, phone: {self.phone}, address: {self.address}, ' \
               f'date_registration: {self.date_of_registration}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # максимум чисел 8 и мест после запятой 2
    description = models.TextField()  # максимальный размер текстового поля по умолчанию
    quantity_of_goods = models.IntegerField(default=0)
    product_update_date = models.DateTimeField(date)
    photo = models.ImageField(upload_to='photos/%y/%m%d/')


class Order(models.Model):
    customer = models.ForeignKey(Client,
                                 on_delete=models.CASCADE)  # заказчик, ссылка на пользователя и при удалении пользователя, мы удалим все его заказы
    products = models.ManyToManyField(
        Product)  # много заказов могут содержать данный продукт и много продуктов могут быть в заказе
    date_ordered = models.DateTimeField(auto_now_add=True)  # при заказе автоматически ставится дата и время
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
