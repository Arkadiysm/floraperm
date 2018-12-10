from django import forms


class CartAddProduct(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)