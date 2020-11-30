"""
core views.

Vues
"""

# > Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

# > Settings
from myhvacrguide.settings import base as settings


class IndexView(generic.TemplateView):
    """
    Index.

    Page publique de presentation du site
    """

    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        """
        Redirection vers le BE CENTER.

        Si login encore actif, renvois au BE CENTER
        en lieu et place de l'index.
        """
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().get(
            request, *args, **kwargs)


class BecenterView(LoginRequiredMixin, generic.TemplateView):
    """
    BE Center.

    Dashboard utilisateur
    """

    template_name = "becenter/becenter.html"
