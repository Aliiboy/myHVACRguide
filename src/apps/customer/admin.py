"""
customer Administration.

Mise en page et presentation

"""

# > Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# > Models
from customer.models import (
        CustomUser,
)


class CustomUserAdmin(UserAdmin):
    """
    Interface Utilisateur.

    config des champs supplementaires
    """

    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
