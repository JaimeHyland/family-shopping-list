from django.shortcuts import render
from django.views import generic
from .models import List_item
from django.contrib.auth.decorators import login_required

# Create your views here.

class ItemListView(generic.ListView):
    queryset = List_item.objects.filter(bought=False)
    template_name = 'shopping_list.html'
    paginate_by = 12
    current_list = List_item.objects.all()