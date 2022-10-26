from django.contrib import admin

from .models import ProductArticle, ExcelArticle


class ProductAdmin(admin.ModelAdmin):
    list_display = ['article', 'brand', 'title']


admin.site.register(ProductArticle)
admin.site.register(ExcelArticle)
