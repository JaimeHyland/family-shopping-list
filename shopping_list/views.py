from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import List_item, Product
from django.contrib.auth.decorators import login_required
from tools.utilities import get_current_user


# Create your views here.

class ItemListView(generic.ListView):
    
    queryset = List_item.objects.filter(bought=False)
    paginate_by = 12
    current_list = List_item.objects.all()

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return 'shopping_list/list_item_list.html'
        else:
            return 'logged_out_homepage.html'


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
        if 'cancelled_item' in request.POST:
            item_id = request.POST.get('cancelled_item')
            item = List_item.objects.get(id=item_id)
            item.cancelled = not item.cancelled
            item.save()
        elif 'completed_items' in request.POST:
            item_id = request.POST.get('completed_items')
            item = List_item.objects.get(id=item_id)
            item.bought = not item.bought
            item.save()
        return redirect('shopping_list')


    def product_detail(request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'shopping_list/product_detail.html', {'product': product})

    def update_shopping_list(request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
        "shopping_list",
        {
            "type": "shopping_list_update",
            "message": "A new item has been added to the shopping list.",
        },
    )
    
    