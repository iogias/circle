from django.contrib import admin

from .models import Promo


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'started', 'ended', 'is_active', 'created')
    list_filter = ('started', 'ended', 'is_active')
    list_editable = ('started', 'ended', 'is_active')
    prepopulated_fields = {'slug': ('title',)}


# class MarketingAdmin(admin.AdminSite):
#     site_header = 'Marketing and Promotion Dashboard'


# promo_marketing_admin = MarketingAdmin(name='Marketing Administration')
# admin.site.register(Promo)
# promo_marketing_admin.register(Promo)
