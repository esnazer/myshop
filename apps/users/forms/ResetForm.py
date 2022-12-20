from django import forms
from django.core import validators
from django.contrib.auth import authenticate, login as django_login, get_user_model

from cuenta.models import Usuario, TokenIU

UserModel = get_user_model()

class ResetForm(forms.Form):
    email = forms.EmailField(min_length=7, widget=forms.TextInput(attrs={
        'placeholder': 'ejemplo: john@gamil.com',
        'class': 'form-control',
        'id': 'iduser'
        }))

    def is_valid(self):
        valido = super().is_valid()
        rmail=self.cleaned_data['email']
        try:
            if Usuario.objects.get(email=rmail):
                pass
        except:
            check_user = False #Es valido cuando no hay usuario
        else:
            check_user = True #No es valido si hay usuario
        if valido and check_user:
            return check_user
        else:
            return False

class ChangePassForm(forms.Form):
    account = forms.CharField(widget=forms.HiddenInput())
    token = forms.CharField(widget=forms.HiddenInput())
    password = forms.CharField(min_length=4, widget = forms.PasswordInput(attrs={
        'placeholder': 'nueva contraseña',
        'class': 'form-control',
        'id': 'iduser'
    }))
    repassword = forms.CharField(min_length=4, widget = forms.PasswordInput(attrs={
        'placeholder': 'repetir contraseña',
        'class': 'form-control',
        'id': 'iduser'
    }))
    
    def is_valid(self):
        valido = super().is_valid()
        checkpw = False
        account = self.cleaned_data['account']
        password = self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']
        if password == repassword:
            checkpw = True
            try:
                user = Usuario.objects.get(email=account)
            except:
                print('algo fallo')
            else:
                user.set_password(password)
                user.save()
        if valido and checkpw:
            return True
        else:
            return False
        
class VerfForm(forms.Form):
    key = forms.CharField(min_length=7, widget=forms.TextInput(attrs={
        'placeholder': 'codigo enviado al correo',
        'class': 'form-control',
        'id': 'iduser'
        }))
    
    def is_valid(self):
        valido = super().is_valid()
        key = self.cleaned_data['key']
        try:
            tokn = TokenIU.objects.get(clave=key)
        except:
            return False
        else:
            account = tokn.usuario
            user = Usuario.objects.get(email=account)
            user.usuario_verificado = True
            tokn.activado = True
            tokn.save()
            user.save() 
            return True