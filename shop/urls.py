from django.urls import path
from .views import *

urlpatterns = [
    path('sale/', record_sale, name='record_sale'),
    path('products/', product_list, name='product_list'),
    path('send-report/', send_daily_report, name='send_report'),
    path('index/', index, name='index'),
    path('inventory/', inventory, name='inventory'),
    path('Reports/', Reports, name='Reports'),
    path('add_product/', add_product, name='add_product'),
    path('Total_Sales/', Total_Sales, name='Total_Sales'),
    path('base/', base, name='base'),
    path('User_Accounts/', User_Accounts, name='User_Accounts'),
    path('delete_product/<int:id>',delete_product, name='delete_product'),
    path('search_suggestions/', search_sugestions, name='search_suggestions'),
]
