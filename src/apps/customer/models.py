"""
customer models.

Models comprenant :
    - Compte utilisateur
"""

# > Django
from django.db import models
from django.utils.translation import gettext_lazy as _
# > Django Models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Utilisateurs.

    Modifier/ajouter des champs supplémentaires ici
    """

    first_name = models.CharField(_('prénom'), max_length=30, blank=True)
    last_name = models.CharField(_('nom'), max_length=30, blank=True)

    def __str__(self):
        return self.email
