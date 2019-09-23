from django.contrib import admin

# Register your models here.
from .models import Product

from .models import Offer

from .models import Addtocart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


class AddtocartAdmin(admin.ModelAdmin):
   list_display = ('code','name','user','dateoforder')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Addtocart, AddtocartAdmin)
