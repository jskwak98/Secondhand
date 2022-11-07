from django import forms
from .models import Sale, Bid


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale  # 사용할 모델
        fields = ['product', 'description', 'price']
        labels = {
            'product': 'Product Name',
            'price': 'Price',
            'description': 'Description',
        }


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['content']
        labels = {
            'content': 'Comment',
        }