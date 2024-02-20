from django.urls import path

from . import views  # or . import views

urlpatterns = [
    path('', views.index, name=''),
    path('game_roll', views.game_roll, name='game_roll'),
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
    path('client/<int:client_id>', views.show_orders, name='show_orders'),
    path('product_list', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),

]
