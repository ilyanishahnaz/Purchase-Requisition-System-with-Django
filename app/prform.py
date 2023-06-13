from django import forms
from django.forms import ModelForm
from .models import PurchaseRequisition
from .models import PR_Item

# Create a PR form

class PRForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequisition
        fields = ('formID',  'empID', 'managerID', 'formDate', 'requiredBy', 'delAddress')

        labels = {
            'formID': 'Form ID',
            'empID': 'Employee',
            'managerID': 'Manager ID',
            'formDate': 'Date of the Form (yyyy-mm-dd)',
            'requiredBy': 'Date of the Delivery (yyyy-mm-dd)',
            'delAddress': 'Delivery Address'
        }

        widgets = {
            'formID': forms.TextInput(attrs={'class': 'form-control', 'placeholder':''}),
            'formDate': forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),
            'requiredBy': forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),
            'delAddress': forms.TextInput(attrs={'class': 'form-control'})
        }
    
class PR_Item_Form(ModelForm):
    class Meta:
        model = PR_Item

        fields = ('itemID','formID','itemName','quantity','unitPrice','totalPrice')

        labels = {
            'formID': 'Form ID (select the last option ONLY)',
        }

        widgets = {
            'itemID' : forms.TextInput(attrs={'class':'form-control'}),
            'formID' : forms.Select(attrs={'class':'form-control'}),
            'itemName' : forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
            'unitPrice' : forms.TextInput(attrs={'class':'form-control'}), 
            'totalPrice' : forms.TextInput(attrs={'class':'form-control'}),
        }
    


        