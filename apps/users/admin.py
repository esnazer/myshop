from django.contrib import admin

# Register your models here.
from apps.users.models import User, Location, UserDate

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','nombres','usuario_activo')
    prepopulated_fields = {'email':('nombres',),}

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('user','state','city','default')


@admin.register(UserDate)
class UserDateAdmin(admin.ModelAdmin):
    list_display = ('user','telf')