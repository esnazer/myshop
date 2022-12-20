from django import forms
import cuenta.tools.options as options

class AccountForm(forms.Form):
       
    nombres = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Nombres',
        'v-model': 'me.nombres',
        'class': 'form-control',
        'id': 'idnombres'
        }))
    apellidos = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Apellidos',
        'v-model': 'me.apellidos',
        'class': 'form-control',
        'id': 'idapellidos'
        }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Telefono',
        'v-model': 'me.phone',
        'class': 'form-control',
        'id': 'idphone'
        }))
    imagen = forms.FileField(required=False, label='Imagen de Perfil')
    public = forms.BooleanField(required=False)
    
class PlaceForm(forms.Form):
    country = forms.ChoiceField(choices=options.country_support,widget=forms.Select(attrs={
        'placeholder': 'pais',
        'v-model': 'me.country',
        'class': 'form-control',
        'id': 'idpais'
        }))
    postalcode = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Codigo Postal',
        'v-model': 'me.postalcode',
        'class': 'form-control',
        'id': 'idpostalcode'
        }))
    street = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Calle y Numero',
        'v-model': 'me.street',
        'class': 'form-control',
        'id': 'idstreet'
        }))
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Ciudad',
        'v-model': 'me.city',
        'class': 'form-control',
        'id': 'idcity'
        }))
    stateorprov = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Estado o Provincia',
        'v-model': 'me.stateorprov',
        'class': 'form-control',
        'id': 'idstateorprov'
        }))
    
    
class ChangePassForm(forms.Form):
    oldpassword = forms.CharField(min_length=4, label="contraseña actual", widget = forms.PasswordInput(attrs={
        'placeholder': 'contraseña actual',
        'v-model': 'auth.oldpw',
        'class': 'form-control',
        'id': 'idoldpassword'
        }))
    newpassword = forms.CharField(min_length=4, label="contraseña nueva", widget = forms.PasswordInput(attrs={
        'placeholder': 'contraseña nueva',
        'v-model': 'auth.newpw',
        'class': 'form-control',
        'id': 'idnewpassword'
        }))
    repassword = forms.CharField(min_length=4, label="contraseña repetir nueva", widget = forms.PasswordInput(attrs={
        'placeholder': 'repetir contraseña',
        'v-model': 'auth.repw',
        'class': 'form-control',
        'id': 'idrepassword'
        }))
    
class AdvancePaymentForm(forms.Form):
    
    method = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Calle y Numero',
        'class': 'form-control',
        'id': 'idstreet'
        }))