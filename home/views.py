from django.shortcuts import render

from shop.models import Product

# Create your views here.
def homepage(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'home/homepage.html', context)
   


def contact(request):
    return render(request, 'home/contact.html')
