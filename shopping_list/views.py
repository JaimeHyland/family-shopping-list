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


    # change the name of the very abstract and general "object_list" to 
    # the much more descriptive "shopping_list"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopping_list'] = context['object_list']
        return context