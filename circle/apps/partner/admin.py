from django.contrib import admin

from circle.apps.partner.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description', 'credentials', 'endpoint', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
