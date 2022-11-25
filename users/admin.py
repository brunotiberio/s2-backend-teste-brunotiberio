from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = (
        "first_name",
        "last_name",
        "cpf",
        "loja",
    )

    fieldsets = (
        ("Dados de Login", {"fields": ("username", "password")}),
        (
            "Dados Pessoais e Financeiros",
            {"fields": ("first_name", "last_name", "cpf", "loja")},
        ),
    )


admin.site.register(User, UserAdmin)
