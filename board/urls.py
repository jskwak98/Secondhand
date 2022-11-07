from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sale_id>/', views.detail, name='detail'),
    path('bid/create/<int:sale_id>/', views.bid_create, name='bid_create'),
    path('sale/create/', views.sale_create, name='sale_create'),
    path('sale/modify/<int:sale_id>/', views.sale_modify, name='sale_modify'),
    path('sale/delete/<int:sale_id>/', views.sale_delete, name='sale_delete'),
    path('bid/accept/<int:bid_id>/', views.bid_accept, name='bid_accept'),
]
