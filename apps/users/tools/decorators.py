from django.conf import settings
from django.shortcuts import redirect
from functools import wraps
from cuenta.tools.ports import Portkey
from cuenta.models import Usuario


def verify_required(v):
    @wraps(v)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/cuentas/login/?next='+request.path)
        us = Usuario.objects.get(email=request.user.email)
        if not us.usuario_verificado:
            return redirect('/cuentas/verify/?netx='+request.path)
        return v(request, *args, **kwargs)
    return wrap

    