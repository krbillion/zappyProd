from django.urls import path

from . import views

app_name='orders'

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('', views.orders, name='user_orders'),
    path('<id>', views.orderDetail, name='orderDetail'),

]
