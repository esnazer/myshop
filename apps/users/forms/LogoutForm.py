from django.contrib.auth import logout as django_logout

def LogoutForm(request):
    print('deslogueando del sitio')
    django_logout(request)