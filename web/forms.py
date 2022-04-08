#
# from django import forms
# from django.forms.widgets import TextInput, Textarea, HiddenInput, Select
# from web.models import *
# from django.utils.translation import ugettext_lazy as _
#
# class ProductForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Products
# 		exclude = ['creator' ,'updator' ,'auto_id' ,'is_deleted' ,'a_id' ,'tax_excluded_price' ,'code' ,'mrp'
# 		           ,'wholesale_price' ,'wholesale_tax_excluded_price' ,'tax' ,'unit' ,'best_before' ,'packing_charge'
# 		           ,'product_expiry_before' ,'vendor' ,'cost' ,'price']
# 		widgets = {
# 			'name': TextInput(attrs={'class': 'required form-control' ,'placeholder' : 'Name'}),
# 			'code': TextInput(attrs={'class': 'required form-control' ,'placeholder' : 'Code'}),
# 			'net_weight': TextInput(attrs={'class': 'form-control' ,'placeholder' : 'Net Weight'}),
# 			'unit_type': Select(attrs={'class': 'required form-control selectpicker'}),
# 			'stock': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Stock'}),
# 			'tax_excluded_price': TextInput(
# 				attrs={'class': 'number required form-control', 'placeholder': 'Tax Excluded Price'}),
# 			'discount': TextInput(attrs={'class': 'number required form-control', 'placeholder': 'Discount'}),
# 			'low_stock_limit': TextInput(
# 				attrs={'class': 'number required form-control', 'placeholder': 'Low stock limit'}),
# 			'best_before': TextInput(attrs={'class': 'number form-control', 'placeholder': 'Best before'}),
# 			'product_expiry_before': TextInput(attrs={'class': 'number form-control', 'placeholder': 'Expiry limit'}),
# 			'packing_charge': TextInput(attrs={'class': 'number form-control', 'placeholder': 'Packing Charge'}),
# 			'shop': HiddenInput(),
# 		}
# 		error_messages = {
# 			'name': {
# 				'required': _("Name field is required."),
# 			},
# 			'code': {
# 				'required': _("Code field is required."),
# 			},
# 			'unit_type': {
# 				'required': _("Unit type field is required."),
# 			},
# 			'stock': {
# 				'required': _("Stock field is required."),
# 			},
# 			'cost': {
# 				'required': _("Cost field is required."),
# 			},
# 			'mrp': {
# 				'required': _("MRP field is required."),
# 			},
# 			'price': {
# 				'required': _("Price field is required."),
# 			},
# 			'tax_excluded_price': {
# 				'required': _(" Tax Excluded Price field is required."),
# 			},
# 			'tax_category': {
# 				'required': _("Tax category field is required."),
# 			},
# 			'discount': {
# 				'required': _("Discount field is required."),
# 			},
# 			'low_stock_limit': {
# 				'required': _("Low stock limit field is required."),
# 			},
#
# 		}
#
# 		help_texts = {
# 			'low_stock_limit': 'You will get one notification when reach this limit',
# 			'tax': 'Tax in Percentage',
# 			'discount': 'Discount in Rupees',
# 			'product_expiry_before': 'You will get one expiry notification when reach this limit',
# 		}
#
# 		labels = {
# 			'product_expiry_before': 'Expiry notification',
# 			'price': 'Selling Price',
# 			'mrp': 'MRP'
# 		}