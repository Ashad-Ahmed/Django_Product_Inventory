# -*- coding: utf-8 -*-
from django.urls import include, path
from products import views
from products.views import func_view

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('view/<int:pk>', views.ProductDetail.as_view(), name='product_view'),
    path('new', views.ProductCreate.as_view(), name='product_new'),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
    path('Func_View',func_view),
    path('api' , views.ProductView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]