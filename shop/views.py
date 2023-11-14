from django.shortcuts import render, get_object_or_404

from .models import Item, Category

# Create your views here.
def detail_product(request, category_slug, slug):
    item = get_object_or_404(Item, slug=slug)

    context = {
        'item': item
    }

    return render(request, 'shop/detail_products.html', context)


def detail_categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    items = category.items.all()

    context = {
        'category': category,
        'items': items,
    }

    return render(request, 'shop/detail_category.html', context)

