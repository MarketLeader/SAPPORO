# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from app.models import Service

import requests
from requests.exceptions import RequestException


class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"),
                       required=True, help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ServiceAdditionForm(forms.Form):
    service_name = forms.SlugField(label=_(
        "Service Name"), max_length=256, required=True, help_text=_("Required.Required. Letters, digits and -/_ only."))
    api_server_url = forms.CharField(label=_(
        "API server url"), max_length=256, required=True, help_text=_("Required. e.g. localhost:8000"))

    def clean(self):
        cleaned_data = super().clean()
        service_name = cleaned_data.get("service_name")
        api_server_url = cleaned_data.get("api_server_url")
        try:
            r = requests.get("http://" + api_server_url + "/service-info")
        except RequestException:
            raise forms.ValidationError("Please enter the correct URL.")
        if Service.objects.filter(name=service_name).exists():
            raise forms.ValidationError(
                "A form with that name already exists.")