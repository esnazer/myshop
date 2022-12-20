from django import forms
from django.core import validators
from django.contrib.auth import authenticate, login as django_login, get_user_model

from cuenta.models import Usuario

UserModel = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(min_length=7, widget=forms.TextInput(attrs={
        'placeholder': 'ejemplo: john@gamil.com',
        'class': 'form-control',
        'id': 'iduser'
        }))
    password = forms.CharField(min_length=1, widget = forms.PasswordInput(attrs={
        'placeholder': 'ejemplo: sucontraseña',
        'class': 'form-control',
        'id': 'iduser'
    }))

    def is_valid(self, request):
        valido = super().is_valid()
        try:
            user = Usuario.objects.get(email=self.cleaned_data['email'])
        except:
            return False
        else:
            return True


    def login(self, request):
        user = authenticate(request, email=self.cleaned_data['email'], password=self.cleaned_data['password'])
        if user:
            django_login(request, user)