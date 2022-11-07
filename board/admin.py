from django.contrib import admin
from .models import Sale, Bid


class SaleAdmin(admin.ModelAdmin):
    search_fields = ['product']

admin.site.register(Sale, SaleAdmin)
# Register your models here.
