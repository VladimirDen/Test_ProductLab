from django.db import models


class ProductArticle(models.Model):
    article = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('article',)


class ExcelArticle(models.Model):
    article = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('article',)
