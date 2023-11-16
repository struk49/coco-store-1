from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from bag import bag

from .models import Item


def api_add_to_bag(request):
    jsonresponse = {'success': True}
    item_id = request.POST.get('item_id')
    update = request.POST.get('update')
    quantity = request.POST.get('quantity', 1)

    bag = Bag(request)

    item = get_object_or_404(Item, pk=item_id)

    if not update:
        bag.add(item=item, quantity=1, update_quantity=False)
    else:
        bag.add(item=item, quantity=quantity, update_quantity=True)

        return JsonResponse(jsonresponse)