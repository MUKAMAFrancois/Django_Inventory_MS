from django import forms
from apps.dashboard.models import ProductModel,OrderModel



class ProductModelForm(forms.ModelForm):

    class Meta:
        model=ProductModel
        fields=['product_name','category','qty','time_of_purchase']


class MakeRequestOrderForm(forms.ModelForm):

    class Meta:
        model=OrderModel
        fields=['name_product','qty_ordered']