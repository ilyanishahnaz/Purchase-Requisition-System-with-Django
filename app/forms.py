"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.forms import DateInput
from app.models import Quotation, Quo_Item
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class QuotationForm(ModelForm):
    class Meta:
        model = Quotation
        fields = ('quoID','vendID', 'formID', 'purchaserID', 'managerID', 'quoDate', 'delAddress')
        widgets = {
            'quoID' : forms.TextInput(attrs={'class':'form-control'}),
            'vendID' : forms.Select(attrs={'class':'form-control'}),
            'formID': forms.Select(attrs={'class':'form-control'}),
            'purchaserID' : forms.Select(attrs={'class':'form-control'}), 
            'managerID' : forms.Select(attrs={'class':'form-control'}),
            'quoDate': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'delAddress' : forms.TextInput(attrs={'class':'form-control'}),
        }

class QuoItemForm(ModelForm):
    class Meta:
        model = Quo_Item
        fields = ('itemID','quoID','itemName','quantity','unitPrice','totalPrice')
        widgets = {
            'itemID' : forms.TextInput(attrs={'class':'form-control'}),
            'quoID' : forms.Select(attrs={'class':'form-control'}),
            'itemName' : forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
            'unitPrice' : forms.TextInput(attrs={'class':'form-control'}), 
            'totalPrice' : forms.TextInput(attrs={'class':'form-control'}),
        }

