from django import forms
from django.shortcuts import get_list_or_404, get_object_or_404, render

from circle.apps.store.models import Category, Item, Product

from .forms import UserInfoForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'store/product/list.html', context)


def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, is_active=True)
    items = get_list_or_404(Item, product_id=id)
    forms = create_forms(slug)
    context = {'product': product, 'items': items, 'categories': categories, 'forms': forms}
    return render(request, 'store/product/detail.html', context)


def create_forms(slug):
    # key_1 = ['arena-of-valor', 'free-fire', 'call-of-duty', 'speed-drifters', 'point-blank'] # user_ip
    key_2 = ['marvel', 'rf-classic']  # server_id
    new_fields = {
        'user_id': forms.CharField(label="User ID", max_length=64,),
    }

    CHOICES_LIFE_AFTER_SERVER = [('000000', '-- PILIH --'),
                                 ('500001', 'MiskaTown (NA)'),
                                 ('500002', 'SandCastle (NA)'),
                                 ('500003', 'MouthSwamp (NA)'),
                                 ('500004', 'RedwoodTown (NA)'),
                                 ('500005', 'Obelisk (NA)'),
                                 ('510001', 'FallForest (AU)'),
                                 ('510002', 'MountSnow (AU)'),
                                 ('520001', 'NancyCity (SEA)'),
                                 ('520002', 'CharlesTown (SEA)'),
                                 ('520003', 'SnowHighlands (SEA)'),
                                 ('520004', 'Santopany (SEA)'),
                                 ('520005', 'LevinCity (SEA)'),
                                 ('500006', 'NewLand (NA)'),
                                 ('520006', 'MileStone (SEA)'), ]
    content = {}
    if slug == 'mobile-legends':
        new_fields["zone_id"] = forms.CharField(label="Zone ID", max_length=20,)
    elif slug == 'life-after':
        new_fields["server_id"] = forms.ChoiceField(label="Server ID", choices=CHOICES_LIFE_AFTER_SERVER)
    elif slug in key_2:
        new_fields["server_id"] = forms.CharField(label="Server ID", max_length=20,)
    else:
        new_fields["user_ip"] = forms.CharField(label="", widget=forms.HiddenInput(), initial="192.168.1.1")

    DynamicForm = type('DynamicForm', (UserInfoForm,), new_fields)
    UserForm = DynamicForm(content)
    return UserForm
