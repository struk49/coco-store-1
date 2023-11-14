from django.shortcuts import render

from shop.models import Item

# Create your views here.
def homepage(request):
    items = Item.objects.filter(featured_item=True)

    context = {
        'items': items
    }

    return render(request, 'home/homepage.html', context)


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')
