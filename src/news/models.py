from django.db import models


class CompanyNews(models.Model):
    id = models.BigIntegerField(primary_key=True)
    stock = models.TextField(max_length=5, null=False)
    headline = models.TextField(null=True)
    image = models.URLField(null=True, max_length=300)
    summary = models.TextField(null=True)
    source = models.TextField(null=False)
    url = models.URLField(null=False, max_length=300)
    published_at = models.DateTimeField(null=False)
