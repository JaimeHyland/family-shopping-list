from . import views
from django.urls import path

urlpatterns = [
    path('', views.ShoppingListView.as_view(), name='shopping_list'),
]
