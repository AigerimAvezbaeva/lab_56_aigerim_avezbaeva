from django.urls import path
from ecom_app.views.base import index_view

from ecom_app.views.products_view import product_view, add_product, update_product, delete_product, \
    confirm_delete

urlpatterns = [
    path('', index_view, name='index'),
    path('product/', index_view, name='index'),
    path('product/<int:pk>', product_view, name='product_detail'),
    path('product/add', add_product, name='add_product'),
    path('product/<int:pk>/update', update_product, name='update_product'),
    path('product/<int:pk>/delete', delete_product, name='delete_product'),
    path('product/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete')
]
