from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credentials', 'endpoint', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
