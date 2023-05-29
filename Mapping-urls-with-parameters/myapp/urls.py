from django.urls import path
from myapp import views 

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drinks"),
        ]