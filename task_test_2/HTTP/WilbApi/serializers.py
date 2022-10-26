from rest_framework import serializers
from .models import *


class ProductArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductArticle
        fields = ['article', 'brand', 'title']


class ProductExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelArticle
        fields = ['article', 'brand', 'title']
