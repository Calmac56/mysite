from django.urls import path
from mysiteapp import views

app_name = 'mysiteapp'

urlpatterns = [
    path('', views.index, name='index'),
]