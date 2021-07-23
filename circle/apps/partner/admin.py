from circle.apps.partner.models import Partner
from django.contrib import admin


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description', 'credentials', 'endpoint', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
