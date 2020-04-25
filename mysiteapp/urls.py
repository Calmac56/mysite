from django.urls import path
from mysiteapp import views

app_name = 'mysiteapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project, name='projects'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/<int:projid>/', views.updateviews, name='updateviews'),
  
]