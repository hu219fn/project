from django.urls import path
from .views import *
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index0'),
    path('register/', SignupView.as_view(), name='register0'),
    path('register/login/', authViews.LoginView.as_view(template_name='ar/auth/login.html',success_url='/ar/'), name='login0'),
    path('register/logout/', Logout, name='logout0'),
    path('register/change-password/', authViews.PasswordChangeView.as_view(template_name='ar/auth/change-password.html', success_url='/ar/register/change-password/done/'), name='change-password0'),
    path('register/change-password/done/', authViews.PasswordChangeDoneView.as_view(template_name='ar/auth/change-password-done.html'), name='password-change-done0'),
    path('search/', Search.as_view(), name='search0'),
    path('<int:id>/', detail, name='detail0'),
    path('orders/', orders, name='orders0'),
    path('order-delete/<int:id>/', order_delete, name='order-delete0'),
    path('management/', management, name='management0'),
    path('management/product-add/', Product_add.as_view(), name='product-add0'),
    path('management/product-orders/<int:id>/', product_order, name='product-order0'),
    path('management/product-edit/<int:pk>/', Product_edit.as_view(), name='product_edit0'),
    path('management/product-delete/<int:id>/', product_delete, name='product_delete0'),
    path('management/users/', users, name='users0'),
    path('management/users/<int:id>/', user, name='user0'),
    path('management/users/delete/<int:id>/', users_delete, name='users_delete0'),
    path('management/users/search/', Search_user.as_view(), name='search-user0'),
    path('management/users/search-ar/', Search_user0.as_view(), name='search-user-ar0'),
    ###########
    path('mini/', mini, name='mini0'),
    path('classic/', classic, name='classic0'),
    path('cards/', cards, name='cards0'),
    path('wood/', wood, name='wood0'),
    path('accessories/', accessories, name='accessories0'),
    path('key-chain/', key_chain, name='key-chain0'),
    path('phone-bag/', phone_bag, name='phone_bag0'),
]
