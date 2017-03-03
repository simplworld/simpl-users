# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import User


class EmailUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', )

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError(_("This email address is already taken"))


class EmailUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_form = EmailUserCreationForm
    ordering = ('email', )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')


admin.site.register(User, EmailUserAdmin)
