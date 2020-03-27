# in urls.py of the application

from django.urls import path

from . import views

app_name = 'Rtournage'
urlpatterns = [
    path('', views.index, name='index'),
    path('statistic/', views.statistic, name='statistic'),
    path('category/', views.category, name='category'),
    path('delcat/<int:id>/', views.del_cat, name="del_cat"),
    path('editcat/', views.edit_cat, name="edit_cat"),
    path('addcat/', views.add_cat, name="add_cat"),
    path('delprod/<int:id>/', views.del_prod, name="del_prod"),
    path('editprod/', views.edit_prod, name="edit_prod"),
    path('addprod/', views.add_prod, name="add_prod"),
    path('buy/', views.buy, name='buy'),
    path('delbuy/<int:id>/', views.del_buy, name="del_buy"),
    path('addbuy/', views.add_buy, name="add_buy"),
    path('sell/', views.sell, name='sell'),
    path('addsell/', views.add_sell, name="add_sell"),
    path('delsell/<int:id>/', views.del_sell, name="del_sell"),
]
