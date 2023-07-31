from django.contrib import admin
from apps.dashboard.models import ProductModel,OrderModel


admin.site.site_header="Inventory MS Dashboard_MUKAMA"
# Register your models here.
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['product_name','qty','category']
    list_filter=['category','time_of_purchase']

    ordering=('time_of_purchase',)

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=['name_product','qty_ordered','client_name']
    list_filter=['client_name','time_of_order']
    ordering=('time_of_order',)