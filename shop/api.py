import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from bag import bag

from .models import Item


def api_add_to_bag(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    item_id = data['item_id']
    update = data['update']
    quantity = data['quantity']

    bag = Bag(request)

    item = get_object_or_404(Item, pk=item_id)

    if not update:
        bag.add(itemt=itemt, quantity=1, update_quantity=False)
    else:
        bag.add(itemt=item, quantity=quantity, update_quantity=True)
    
    return JsonResponse(jsonresponse)