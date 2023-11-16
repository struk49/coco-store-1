from django.shortcuts import render

from .bag import Bag

# Create your views here.
def bag_detail(request):
    bag = Bag(request)
    productsstring = ''

    for item in bag:
        item = item['item']
        url = '/%s/%s/' % (item.category.slug, item.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (item.id, item.title, item.price, item['quantity'], item['total_price'], item.get_thumbnail, url, item.num_available)

        productsstring = productsstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        address = request.user.userprofile.address
        zipcode = request.user.userprofile.zipcode
        place = request.user.userprofile.place
        phone = request.user.userprofile.phone
    else:
        first_name = last_name = email = address = zipcode = place = phone = ''

    context = {
        'bag': bag,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'zipcode': zipcode,
        'place': place,
       
    }

    return render(request, 'bag.html', context)

