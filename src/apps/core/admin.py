"""
core Administration.

Mise en page et presentation

"""

# > Django
from django.contrib import admin
# > Models
from core.models import (
        CustomSite,
)


class CustomSiteAdmin(admin.ModelAdmin):
    """
    Interface CustomSite.

    config des champs supplementaires
    """

    model = CustomSite
    list_display = ['site', 'signup', ]


admin.site.register(CustomSite, CustomSiteAdmin)
