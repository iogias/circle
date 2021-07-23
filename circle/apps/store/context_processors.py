from .models import Category


def menu_categories(request):
    categories = Category.objects.filter(is_active=True)
    return {'menu_categories': categories}
