from django.shortcuts import render, get_object_or_404

from .models import Product, Category

# Create your views here.
def detail_product(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'shop/detail_products.html', context)


def detail_categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'shop/detail_category.html', context)

