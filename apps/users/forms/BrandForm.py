from django import forms
from froala_editor.widgets import FroalaEditor
from ckeditor.widgets import CKEditorWidget
import cuenta.tools.options as options

class BrandDateForm(forms.Form):
    name = forms.CharField(max_length=50, label='Nombre', widget=forms.TextInput(attrs={
        'placeholder': 'Nombre',
        'class': 'form-control',
        'id': 'idnombre'
        }))
    description = forms.CharField(widget=CKEditorWidget())
    sector = forms.ChoiceField(label='Sector',choices=options.brand_subsector)
    logo = forms.FileField(required=False, label='Logo de la Marca Personal')
    
class ProductDetailForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    short_description = forms.CharField(max_length=200, widget=forms.Textarea, required=False)
    price = forms.NumberInput()
    stock = forms.BooleanField(required=False)
    available = forms.BooleanField(required=False)
    
class ProductImagenDetailForm(forms.Form):
    file = forms.ImageField()