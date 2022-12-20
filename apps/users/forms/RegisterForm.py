from django import forms
from django.core import validators
from django.contrib.auth import authenticate, login as django_login, get_user_model

from cuenta.models import Usuario, TokenIU, SuscriptionIU

from hashlib import shake_256
import datetime

UserModel = get_user_model()

class RegisterForm(forms.Form):
    email = forms.EmailField(min_length=7, widget=forms.TextInput(attrs={
        'placeholder': 'ejemplo: john@gamil.com',
        'class': 'form-control',
        'id': 'iduser'
        }))
    password = forms.CharField(min_length=1, widget = forms.PasswordInput(attrs={
        'placeholder': 'nueva contraseña',
        'class': 'form-control',
        'id': 'iduser'
    }))
    repassword = forms.CharField(min_length=1, widget = forms.PasswordInput(attrs={
        'placeholder': 'repita contraseña',
        'class': 'form-control',
        'id': 'iduser'
    }))

    def is_valid(self):
        valido = super().is_valid()
        checkpw = False
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['repassword']
        if p1 == p2:
            checkpw = True
        try:
            if Usuario.objects.get(email=self.cleaned_data['email']):
                pass
        except:
            check_user = True #Es valido cuando no hay usuario
        else:
            check_user = False #No es valido si hay usuario
        if valido and checkpw and check_user:
            return True
        else:
            return False


    def login(self, request):
        user = authenticate(request, email=self.cleaned_data['email'], password=self.cleaned_data['password'])
        if user:
            django_login(request, user)


    def register(self, request):
        correo = self.cleaned_data['email']
        passw = self.cleaned_data['password']
        user = UserModel.objects.create_user(email=correo, password=passw)
        user.save()
        self.login(request)
        