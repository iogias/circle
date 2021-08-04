from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from circle.apps.core.views import (faq, home, kontak_kami, syarat_ketentuan,
                                    tentang_kami)

urlpatterns = [
    path('reign/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', home, name='home'),
    path('tentang-kami/', tentang_kami, name='tentang_kami'),
    path('faq/', faq, name='faq'),
    path('syarat-ketentuan/', syarat_ketentuan, name='syarat_ketentuan'),
    path('kontak-kami/', kontak_kami, name='kontak_kami'),
    path('toko/', include('circle.apps.store.urls', namespace='store')),
    path('promo/', include('circle.apps.promo.urls', namespace='promo')),
    path('cart/', include('circle.apps.cart.urls', namespace='cart')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = 'YODU Circle Dashboard'
admin.site.site_header = 'CMS YODU Circle'
admin.site.site_title = 'Site Admin'
