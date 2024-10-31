from django import forms
from category.models import CategoryModel
class category_form(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields='__all__'