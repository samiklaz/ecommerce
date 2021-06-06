from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', product, name='product'),
    path('<slug>/', ProductDetailView.as_view(), name='details'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),

]
