from django.contrib import admin

from circle.apps.store.models import Category, Item, Product, Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'list_products', 'is_active')
    prepopulated_fields = {'slug': ('name',)}

    def list_products(self, obj):
        result = Product.objects.filter(store=obj, is_active=True).only('name')
        return list(result)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'slug', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name__startswith', )
    list_display = ('name', 'product_code', 'category', 'attribute', 'is_active')
    list_filter = ('category', 'attribute', 'is_active')
    list_editable = ('product_code', 'category', 'attribute', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name__startswith', )
    list_display = ('name', 'product', 'partner', 'item_code', 'buy_price', 'sell_price', 'attribute', 'is_active')
    list_filter = ('partner', 'product', 'attribute', 'is_active')
    list_editable = ('partner', 'item_code', 'buy_price', 'sell_price', 'attribute', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
