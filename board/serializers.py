from rest_framework import serializers
from .models import Sale, Bid

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'price', 'product', 'seller_id')


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('buyer_id', 'agreed', 'sale_id')