from django.contrib import admin

from .models import Goods, Order

admin.site.register(Goods)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'customer_name', 'phone_num', 'address',
                       'date', 'goods', 'total_sum', 'comment', 'payed']
