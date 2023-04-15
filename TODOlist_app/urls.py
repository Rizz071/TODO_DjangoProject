from django.urls import path
from . import views


app_name = 'TODOlist_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]