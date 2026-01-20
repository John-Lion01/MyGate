from django import forms
from .models import Message
from django.utils.translation import gettext_lazy as _

class MessageForm(forms.ModelForm) :
    full_name = forms.CharField(
        label='',
        required=True,
        strip=False,
        widget=forms.TextInput(attrs={
            "autocomplete" : "full_name",
            "placeholder" : _("Nom et prénom")
        })
    )
    email = forms.CharField(
        label='',
        required=True,
        strip=False,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            "placeholder": _("address e-mail")
        })
    )
    sujet = forms.CharField(
        label='',
        required=False,
        strip=False,
        widget=forms.TextInput(attrs={
            "autocomplete": "sujet",
            "placeholder": _("Sujet")
        })
    )
    message = forms.CharField(
        label='',
        required=True,
        strip=False,
        widget=forms.Textarea(attrs={
            "autocomplete": "message",
            "placeholder": _("Entrer votre message ..."),
            "rows" : 3
        })
    )
    class Meta :
        model = Message
        fields = ["full_name", "email", "sujet", "message"]