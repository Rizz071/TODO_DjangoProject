from django.urls import path
from . import views


app_name = 'TODOlist_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_list/', views.add_list, name='add_list'),
    path('del_list/', views.del_list, name='del_list'),
]