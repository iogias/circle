from django.shortcuts import get_object_or_404, render

from .models import Promo


def promo_list(request):
    promo_list = Promo.objects.order_by('-started')[:5]
    context = {'promo_list': promo_list}
    return render(request, 'promo/list.html', context)


def promo_detail(request, id, slug):
    promo = get_object_or_404(Promo, id=id, slug=slug, is_active=True)
    context = {'promo': promo}
    return render(request, 'promo/detail.html', context)
