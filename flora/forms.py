from django import forms


class DeliveryForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=25, required=False)
    phone_num = forms.CharField(max_length=10)
    street = forms.CharField(max_length=40)
    street_number = forms.CharField(max_length=5)
    flat_number = forms.CharField(max_length=5, required=False)
    additional_directions = forms.CharField(max_length=200 ,widget=forms.Textarea, required=False)


