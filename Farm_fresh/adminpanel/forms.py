from django import forms
from .models import Product, Category



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control'}),
            'discounted_price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'composition': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control'})
        }
    def __init__(self, *args, **kwargs):

        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category_image': forms.FileInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'form-control'}),
        }


