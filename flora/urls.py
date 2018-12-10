from django.urls import path
from . import views
from .models import Goods


urlpatterns = [
    path('', views.index),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<str:category>/', views.catalog_categories, name='catalog-categories'),
    path('add_goods/', views.add_goods, name='add_goods'),
    path('remove_goods/', views.remove_goods, name='remove_goods'),
]

for i in Goods.GOODS_TYPES:
    urlpatterns.append(path('catalog/'+r'{}/add_goods/'.format(i[0].lower()), views.add_goods, name="add_goods"))
    urlpatterns.append(path('catalog/' + r'{}/remove_goods/'.format(i[0].lower()), views.remove_goods, name="remove_goods"))