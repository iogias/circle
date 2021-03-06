from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from circle.apps.partner.models import Partner


def inquiry_item(request):
    if request.is_ajax and request.method == 'POST':
        res = request.POST.dict()
        partner = get_object_or_404(Partner, id=res['partner_id'], is_active=True)

        if partner.code == 'upoint':
            result = partner.upoint_dtu_inquiry(res['item_code'])
            msg = True
        elif partner.code == 'upoint_voucher':
            result = partner.upoint_voucher_request(res['item_code'])
            msg = True
        elif partner.code == 'razer_voucher':
            result = partner.razer_voucher_check_stock(res['product_code'])
            msg = True
        else:
            result = 'Not Found'
            msg = False
        response = dict(message=msg, data=result)
        return JsonResponse(response)
