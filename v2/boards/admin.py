from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Revisa si 'email' y 'phone_number' ya están presentes para evitar duplicados
    fieldsets = list(UserAdmin.fieldsets)  # Copia el fieldset predeterminado
    fieldsets[1] = (  # Modifica el fieldset de "Información Personal"
        'Personal Information',
        {'fields': ('first_name', 'last_name', 'email', 'phone_number')},  # Añade phone_number
    )

