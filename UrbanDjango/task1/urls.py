from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.menu_page, name='menu_page'),
    path('', views.main_page, name='main_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('bin/', views.bin_page, name='bin_page'),
    path('game/', views.collect_of_games, name='collect_of_games'),
    path('django_sign_up/', views.sign_up_by_django, name='django_sign_up'),
    path('html_sign_up/', views.sign_up_by_html, name='html_sign_up'),
]