from . import views
from django.urls import path

urlpatterns = [
    path('', views.ItemListView.as_view(), name='shopping_list'),
]
