from django.contrib import admin

# Register your models here.
from apps.shop.models import Category, Product, Multimedia, Store, Stock

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','code','unit','brand')

@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
    list_display = ('tag','type','file')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('product','code','amount','cost')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('store','code','price')