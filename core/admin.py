from django.contrib import admin
from .models import Item, OrderItem, Order, Payments, BillingAddress, DiscountCode

class OrderAdmin(admin.ModelAdmin):
    list_display=['user', 'is_ordered']

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payments)
admin.site.register(BillingAddress)
admin.site.register(DiscountCode)

