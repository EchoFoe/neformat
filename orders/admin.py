from django.contrib import admin
from .models import *

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

    class StatusAdmin (admin.ModelAdmin):
        list_display = [field.name for field in Status._meta.fields]

        class Meta:
            model = Status

    admin.site.register(Status, StatusAdmin)

class OrderAdmin (admin.ModelAdmin):
    save_as = True
    fields = [('user', 'total_price', 'Status'), ('customer_name', 'customer_email', 'customer_phone'), 'customer_address']
    # list_display = [field.name for field in Order._meta.fields]
    list_display = ['id', 'user', 'customer_name', 'customer_email', 'customer_address', 'total_price', 'Status', 'created' ]
    inlines = [ProductInOrderInline]
    search_fields = ['customer_name', 'customer_phone']
    list_filter = ['Status']

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)

class ProductInBasketAdmin (admin.ModelAdmin):
    # list_display = [field.name for field in ProductInBasket._meta.fields]
    list_display = ['id', 'order', 'product', 'nmb', 'price_per_item', 'total_price', 'created', 'is_active']

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)
