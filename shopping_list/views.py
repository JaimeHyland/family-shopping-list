from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import List_item, Product
from django.contrib.auth.decorators import login_required
from tools.utilities import get_current_user


# Create your views here.

class ItemListView(generic.ListView):
    queryset = List_item.objects.filter(bought=False)
    template_name = 'shopping_list.html'
    paginate_by = 12
    current_list = List_item.objects.all()

    def dispatch(self, request, *args, **kwargs):
        current_user = get_current_user(request)
        return super().dispatch(request, *args, **kwargs)

    # change the name of the very abstract and general "object_list" to 
    # the much more descriptive "shopping_list"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopping_list'] = context['object_list']
        return context

    def post(self, request, *args, **kwargs):
        return redirect('shopping_list')


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shopping_list/product_detail.html', {'product': product})
    