from .models import Category

def categories_menu(request):
    categories = Category.objects.all()

    return {'categories_menu': categories}