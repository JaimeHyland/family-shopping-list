from django.shortcuts import render
from django.views import generic
from .models import List_item

# Create your views here.

class ItemList(generic.ListView):
    queryset = List_item.objects.filter(bought=False)
    template_name = 'shopping_list/index.html'
    paginate_by = 12