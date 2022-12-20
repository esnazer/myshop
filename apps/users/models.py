
from datetime import timedelta
from hashlib import shake_256

from simple_history.models import HistoricalRecords

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.users.tools.ports import PortMail
from apps.users.tools import options as options

class UsuarioManager(BaseUserManager):
    def create_user(self,email,password = None):
        if not email:
            raise ValueError('El usuario debe tener correo electronico')
        usuario = self.model(
            email = self.normalize_email(email)
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,email,password):
        usuario = self.create_user(email,password=password)
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class User(AbstractBaseUser):

    email = models.EmailField('Correo Electronico', unique = True, max_length=254)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    modified_date = models.DateTimeField('Ultima Modificación', auto_now=True, auto_now_add=False, null=True)
    deleted_date = models.DateTimeField('Fecha de Eliminación', auto_now=True, auto_now_add=False, null=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
    
class BaseModel(models.Model):
    created = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(user_model=settings.AUTH_USER_MODEL, inherit=True)
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

class Location(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    state = models.CharField('Provincia', max_length=200, blank=True, null=True)
    city = models.CharField('Ciudad', max_length=100, blank=True, null=True)
    street = models.CharField('Calle', max_length=200, blank=True, null=True)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

class UserDate(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    telf = models.CharField('Telf', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'User Data'
        verbose_name_plural = 'Datas'