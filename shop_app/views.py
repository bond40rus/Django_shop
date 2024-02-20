import random
import logging
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from .models import Client, Product, Order
from datetime import datetime, timedelta, timezone
from .forms import ProductForm

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('Hello world!')


def game_roll(request):
    rnd_num = random.randint(0, 100)
    logger.info(f'бросок  в игре "game_roll" = {str(rnd_num)}')
    return HttpResponse(f'Вы выбросили {str(rnd_num)} .')


def about(request):
    text = f'<h1> about me. i am Sergey </h1> \n' \
           f'<h2>my telegram Vidok40rus </h2>\n' \
           f'<h3> it is my first shop in Django </h3>'
    return HttpResponse(text, content_type='text/html', charset="utf-8")  # не кодируется


def index(request):
    return render(request, "shop_app/index.html")  # возвращаем шаблон index


def show_orders(request, client_id):
    client = Client.object.get(pk=client_id)
    orders = Order.object.filter(client=client)
    context = {'order': orders}
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client = Client.objects.get(id=client_id)
        days = request.POST.get('report')
        if days == '7':
            orders = Order.objects.filter(client=client, order_date__gte=timezone.now() - timedelta(days=7))
            time_period = 'неделю'
        elif days == '30':
            orders = Order.objects.filter(client=client, order_date__gte=timezone.now() - timedelta(days=30))
            time_period = 'месяц'
        else:
            orders = Order.objects.filter(client=client, order_date__gte=timezone.now() - timedelta(days=365))
            time_period = 'год'
        products = []
        for order in orders:
            products.extend(order.products.all())
        products = list(set(products))
        context.update({
            'client': client,
            'products': products,
            'days': time_period
        })
    return render(request, "shop_app/order_list.html", context)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
