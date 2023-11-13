from django.shortcuts import render

from shop.models import Product

# Create your views here.
def homepage(request):
    products = Product.objects.filter(is_featured=True)

    context = {
        'products': products
    }

    return render(request, 'home/homepage.html', context)


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')
