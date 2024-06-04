from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import List_item, Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from tools.utilities import get_current_user

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ShoppingListView(View):
    def get(self, request, *args, **kwargs):
        shopping_list = List_item.objects.filter(bought=False)
        print(f"Bugfix: GET request by bought status. Items: {shopping_list}")
        return render(request, 'shopping_list/shopping_list.html', {'shopping_list': shopping_list})

    def post(self, request, *args, **kwargs):
        try:
            print(f"Bugfix: POST request data: {request.POST}")
            print(f"Bugfix: POST item_id: {request.POST.get('item_id')}")
            print(f"Bugfix: POST action: {request.POST.get('action')}")
            item_id = request.POST.get('item_id')
            action = request.POST.get('action')

            if not item_id or not action:
                print("Invalid request: Missing item_id or action")
                return HttpResponseBadRequest("Invalid request: Missing item_id or action")

            item = get_object_or_404(List_item, id=item_id)

            if action == 'cancel':
                item.cancelled = True
            elif action == 'uncancel':
                item.cancelled = False
            elif action == 'bought':
                item.bought = True
            elif action == 'unbought':
                item.bought = False
            else:
                return HttpResponseBadRequest("Invalid request: Unknown action")

            item.save()
            return redirect('shopping_list')

        except Exception as e:
            print(f"Error processing POST request: {e}")
            return HttpResponseBadRequest("Invalid request")


    def get(self, request, *args, **kwargs):
        try:
            items = List_item.objects.filter(bought=False)
            print(f"Debug: {items}")
            return render(request, 'shopping_list/shopping_list.html', {'items': items})

        except Exception as e:
            print(f"Error processing GET request: {e}")
            return HttpResponseBadRequest("Invalid request")

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


@login_required
def product_detail(request, slug):
    item = Item.objects.get(product__slug=slug)
    print(f"Product detail for item: {item}")
    return render(request, 'product_detail.html', {'item': item})

    
    