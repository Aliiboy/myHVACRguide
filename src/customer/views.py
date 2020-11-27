"""
customer views.

Vues
"""

# > Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
# > Forms
from customer.forms import (
    ProfileUpdateForm,
)


class ProfileUpdateView(LoginRequiredMixin, generic.FormView):
    """
    Profil.

    Edition du profil utilisateur
    """

    form_class = ProfileUpdateForm
    template_name = 'app/customer/profile_update.html'
    success_url = reverse_lazy('customer:account_profile')

    def get_form_kwargs(self):
        """
        Paramètres.

        Construit les paramètres nommés requis
        pour créer une instance de formulaire.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """
        Conformite du formulaire.

        Si le formulaire est valide, redirigez vers l'URL fournie.
        """
        form.save()
        messages.success(self.request, _("Profil mis à jour"))
        return redirect(self.get_success_url())
