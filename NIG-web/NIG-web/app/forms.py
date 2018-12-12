# coding: utf-8

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _


class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"),
                       required=True, help_text=_("この項目は必須です。"))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user