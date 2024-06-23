from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.products, name='category'),
    path('page/<int:page_number>', views.products, name='paginator'),
    path('product/', views.products, name='product'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
]
