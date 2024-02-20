from django import forms
from .models import Product


class ClientForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity_of_goods', 'photo']
