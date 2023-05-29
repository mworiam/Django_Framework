from django.urls import path 
from . import views
urlpatterns = [
        path('', views.home, name="home"),
        path('about/', views.about),
        path('menu/', views.menu),
        path('book/', views.book, name="book"),
]